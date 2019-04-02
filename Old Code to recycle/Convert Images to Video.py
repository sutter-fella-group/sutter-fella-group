import os
import glob
from shutil import copyfile
from guidata.qt.compat import getexistingdirectory
import guidata

_app = guidata.qapplication()
image_path = getexistingdirectory(None, 'path to images')
#image_path = 'G:/Pictures/04092018-meg/E3-10fps/Separated_tif'
num_convert = 2000
fps = 10
FilesNames = glob.glob(image_path + "\*.png")
temp_name = FilesNames[0].split('t=')
name_root = temp_name[0] + 't='
temp_name = temp_name[1].split('.png')
#time_start = float(temp_name[0])
time_start = -3.0
if os.path.exists(image_path+"/temp"):
    print('temp folder already exists')
else:
    os.mkdir(image_path + '/temp')

i = 0
while i <= num_convert:
    time = time_start + i/fps
    try:
        src = name_root + str(round(time, 1)) + '.png'
        print(src)
        dst = image_path + '/temp/pic' + '%04d' % i + '.png'
        copyfile(src, dst)
    except FileNotFoundError:
        src = name_root + str(round(time)) + '.png'
        print(src)
        dst = image_path + '/temp/pic' + '%04d' % i + '.png'
        copyfile(src, dst)
    i += 1

os.chdir(image_path + '/temp')
os.system('ffmpeg -r 10 -f image2 -s 1280x1024 -i pic%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p E3.mp4')