#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uvctypes import *
import time
from datetime import datetime
import cv2
import png
import numpy as np
try:
  from queue import Queue
except ImportError:
  from Queue import Queue
import platform
import multiprocessing

BUF_SIZE = 2
q = Queue(BUF_SIZE)

def py_frame_callback(frame, userptr):

  array_pointer = cast(frame.contents.data, POINTER(c_uint16 * (frame.contents.width * frame.contents.height)))
  data = np.frombuffer(
    array_pointer.contents, dtype=np.dtype(np.uint16)
  ).reshape(
    frame.contents.height, frame.contents.width
  ) # no copy

  # data = np.fromiter(
  #   frame.contents.data, dtype=np.dtype(np.uint8), count=frame.contents.data_bytes
  # ).reshape(
  #   frame.contents.height, frame.contents.width, 2
  # ) # copy

  if frame.contents.data_bytes != (2 * frame.contents.width * frame.contents.height):
    return

  if not q.full():
    q.put(data)

PTR_PY_FRAME_CALLBACK = CFUNCTYPE(None, POINTER(uvc_frame), c_void_p)(py_frame_callback)

def ktof(val):
  return ktoc(val)

def ktoc(val):
  return (val - 27315) / 100.0

def Normalize(data):
  global mean_substrate
  mean_substrate =np.mean(data[70:80,70:80])
  #data_2 = cv2.normalize(data, None, 0, 65535, cv2.NORM_MINMAX)
  data_2 = cv2.normalize(data, None, 0, 255, cv2.NORM_MINMAX)
  #np.right_shift(data_2, 8, data_2) #divide mat by 256
  return cv2.cvtColor(np.uint8(data_2), cv2.COLOR_GRAY2RGB)
  #return np.uint8(data)

def Substrate(img):
  img_Substrate = img[70:80,70:80]
  print(img_Substrate)
  data_2 = cv2.normalize(img_Substrate, None, 0, 65535, cv2.NORM_MINMAX)
  #np.right_shift(img_Substrate, 8, img_Substrate)
  return np.uint8(img_Substrate)

def display_temperature(img, val_k, loc, color):
  val = ktof(val_k)
  cv2.putText(img,"{0:.1f} degC".format(val), loc, cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
  x, y = loc
  cv2.line(img, (x - 2, y), (x + 2, y), color, 1)
  cv2.line(img, (x, y - 2), (x, y + 2), color, 1)

def main():
  ctx = POINTER(uvc_context)()
  dev = POINTER(uvc_device)()
  devh = POINTER(uvc_device_handle)()
  ctrl = uvc_stream_ctrl()

  res = libuvc.uvc_init(byref(ctx), 0)
  if res < 0:
    print("uvc_init error")
    exit(1)

  try:
    res = libuvc.uvc_find_device(ctx, byref(dev),  0x1e4e, 0x0100, 0)
    if res < 0:
      print("uvc_find_device error")
      exit(1)

    try:
      res = libuvc.uvc_open(dev, byref(devh))
      if res < 0:
        print("uvc_open error")
        exit(1)

      print("device opened!")

      print_device_info(devh)
      print_device_formats(devh)
      print(byref)
      print(byref(ctrl))
      print(ctrl)
      frame_formats = uvc_get_frame_formats_by_guid(devh, VS_FMT_GUID_Y16)
      if len(frame_formats) == 0:
        print("device does not support Y16")
        exit(1)

      libuvc.uvc_get_stream_ctrl_format_size(devh, byref(ctrl), UVC_FRAME_FORMAT_Y16,
        frame_formats[0].wWidth, frame_formats[0].wHeight, int(1e7 / frame_formats[0].dwDefaultFrameInterval)
      )

      res = libuvc.uvc_start_streaming(devh, byref(ctrl), PTR_PY_FRAME_CALLBACK, None, 0)
      if res < 0:
        print("uvc_start_streaming failed: {0}".format(res))
        exit(1)

      try:
        loop_index = 1
        record_start = 0
        while True:
          loop_index += 1
          data = q.get(True, 500)
          if data is None:
            break
          time_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
          if loop_index % 9 == 0:
              if record_start == 1:
                cv2.imwrite('capture_' + time_string + '.png', data)
          img = Normalize(data)
          img_2 = Substrate(data)
          img = cv2.resize(img[:, :], (640, 480))
          img_2 = cv2.resize(img_2[:, :], (200, 200))
          #minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(data)
          display_temperature(img, mean_substrate, (500, 420), (255, 0, 0))
          display_temperature(img_2, mean_substrate, (70, 70), (255, 0, 0))
          im_color = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
          img_2 = cv2.applyColorMap(img_2, cv2.COLORMAP_JET)
          cv2.imshow('Lepton Radiometry_normalized', im_color)
          cv2.imshow('Substrate', img_2)
          if loop_index % 9 == 0:
              if record_start == 1:
                cv2.imwrite ('colored_capture' + time_string + '.png', im_color)

          return_waitkey = cv2.waitKey(1)
          if return_waitkey == 99:
              break

          if return_waitkey == 100:
            if record_start == 0:
              print('Recording Started')
              record_start = 1
            else:
              print('Recording Stopped')
              record_start = 0

        cv2.destroyAllWindows()

      finally:
        libuvc.uvc_stop_streaming(devh)
      print("done")
    finally:
      libuvc.uvc_unref_device(dev)
  finally:
    libuvc.uvc_exit(ctx)
if __name__ == '__main__':
  main()
