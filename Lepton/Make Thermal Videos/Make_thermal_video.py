import cv2
import numpy as np
import os
from os import listdir
import time
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image
import pylab as pl
from guidata.qt.compat import getexistingdirectory
import guidata

def make_big_colorbar():
        a = np.array([[0,150]])
        k = pl.figure(figsize=(1.2, 4.8))
        img = pl.imshow(a, cmap="jet")
        pl.gca().set_visible(False)
        cax = pl.axes([0.1, 0.1, 0.5,0.8])
        pl.colorbar(orientation="vertical", cax=cax)
        pl.savefig("colorbar.jpg")
        pl.close(k)
        colorbar = cv2.imread("colorbar.jpg")
        return colorbar

def make_mini_colorbar():
        a = np.array([[np.min((im[68:80,66:80] - 27315) / 100.0),np.max((im[68:80,66:80] - 27315) / 100.0)]])
        k = pl.figure(figsize=(1.2, 2.4))
        img = pl.imshow(a, cmap="jet")
        pl.gca().set_visible(False)
        cax = pl.axes([0.1, 0.1, 0.5, 0.8])
        pl.colorbar(orientation="vertical", cax=cax)
        pl.savefig("mini_colorbar.jpg")
        pl.close(k)
        mini_colorbar = cv2.imread('mini_colorbar.jpg')
        mini_colorbar = cv2.resize(mini_colorbar,(45,180))
        return mini_colorbar
#dir_path = os.path.dirname(os.path.realpath(__file__))

_app = guidata.qapplication()
dir_path = getexistingdirectory(None, 'path to images')
colorbar = make_big_colorbar()

dirName = os.path.join(dir_path,'new')
try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

filenames = listdir(dir_path)
img_array = []

#text details
fontpath = "./simsun.ttc"
font                   = ImageFont.truetype(fontpath, 32)
bottomLeftCornerOfText = (0,30)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

lineThickness = 2
temp_center = [0]
time = [0]
fig = plt.figure(figsize=(4.2,4.2))
plt.subplot(111)
for i in range(len(listdir(dir_path))):
    if filenames[i].endswith(".png"):
        im = cv2.imread(os.path.join(dir_path,filenames[i]),-1)
        plate = (150-0)/256
        im_8bit = np.round(((im - 27315) / 100.0 - 0) / plate - 1,0)
        im_8bit = np.uint8(im_8bit)
        im_color = cv2.applyColorMap(im_8bit, cv2.COLORMAP_JET)
        im_color = cv2.resize(im_color[:,:],(640, 480))
        im_color = np.concatenate((im_color,colorbar),axis = 1)
        # add in zoomed images
        zoomed = cv2.resize((im[55:85,55:95] - 27315) / 100,(180,180))
        zoomed = cv2.normalize(zoomed, None, 0, 255, cv2.NORM_MINMAX)
        #plot temperature every 15 frames
        temp_center.append(np.mean((im[68:80,66:80] - 27315) / 100.0))
        time.append(i+1)
        if i%15 == 0 or i == 1:
                plt.cla()
                plt.xlabel('Time (s)')
                plt.ylabel('Temperature (ºC)')
                plt.plot(time,temp_center)
                plt.ylim([0,max(temp_center)+10])
                plt.xlim([0, i+5])
                fig.canvas.draw()
                data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8)
                im_size = fig.canvas.get_width_height() 
                data = data.reshape(im_size[1],im_size[0],3)

                #cv2.imshow('123',data)
                #cv2.waitKey(1)
                data = cv2.resize(data,(210,210))

                #make a colorbar as well
                mini_colorbar = make_mini_colorbar()
        zoomed = cv2.applyColorMap(np.uint8(zoomed),cv2.COLORMAP_JET)
        zoomed = np.concatenate((zoomed,mini_colorbar),axis = 1)
        im_color[300:480,415:640] = zoomed
        im_color[270:480,0:210] = data
        im_color = cv2.putText(im_color,str(i//60).zfill(2)+':'+str(i%60).zfill(2), 
                bottomLeftCornerOfText,
                cv2.FONT_HERSHEY_COMPLEX, 
                fontScale,
                (255,255,255),
                lineType)
        img_pil = Image.fromarray(im_color)
        draw = ImageDraw.Draw(img_pil)
        draw.text((500, 20), str(np.round(temp_center[i+1],2))+'ºC', font = font, fill = (0, 255, 0, 128))
        draw.text((500, 50), str(np.round(np.mean((im[40:48,67:86]- 27315) / 100.0),2))+'ºC', font = font, fill = (0, 0, 255, 128))
        im_color = np.array(img_pil)
        cv2.rectangle(im_color, (4*67,4*40), (4*86,4*48), (0,0,255), thickness = 2)
        cv2.rectangle(im_color, (68*4,66*4), (86*4,80*4), (0,255,0), thickness = 2)
        cv2.imwrite(os.path.join(dir_path,'new',filenames[i]),im_color)
        print(i)
height, width, layers = im_color.shape
size = (width,height)
out = cv2.VideoWriter(os.path.join(dir_path,'colored_withscale.avi'),cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
for i in range(len(filenames)):
        imdir = os.path.join(dir_path,'new',filenames[i])
        img = cv2.imread(imdir)
        out.write(img)
out.release()

# add pyrometer temp
# add scale bar for zoomed image