import time
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog
from tkinter import Tk
import glob
from matplotlib import ticker, cm
import matplotlib.animation as animation

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
time_start = time.time()
previous_length = 0
Z = np.array([])

fig=plt.figure()
ax = fig.add_subplot(111)

filenames = glob.glob(folder_selected + "/*.txt")
new_lenth = len(filenames)-2
for i in range(previous_length,new_lenth):
    spectra = np.loadtxt(filenames[i],skiprows = 14)
    if len(Z) == 0:
        Z = np.transpose([spectra[:,1]])
    Z = np.hstack([Z,np.transpose([spectra[:,1]])])
    Y = np.transpose([spectra[:,0]])
#update the length
previous_length = new_lenth
Y = np.transpose(spectra[:,0])
X = np.linspace(0,time.time()-time_start,num = new_lenth+1)
CS = [ax.contourf(X,Y,Z, 20,locator=ticker.LogLocator(), cmap= 'jet') ]
fig.colorbar(CS[0]) 

def animate(k):
    global previous_length
    global CS
    global fig
    global spectra
    global Z
    for tp in CS[0].collections:
        tp.remove()
    filenames = glob.glob(folder_selected + "/*.txt")
    new_lenth = len(filenames)-2
    if new_lenth > previous_length:
        for i in range(previous_length,new_lenth):
            spectra = np.loadtxt(filenames[i],skiprows = 14)
            if len(Z) == 0:
                Z = np.transpose([spectra[:,1]])
            Z = np.hstack([Z,np.transpose([spectra[:,1]])])
            Y = np.transpose([spectra[:,0]])
        #update the length
        previous_length = new_lenth
    Y = np.transpose(spectra[:,0])
    X = np.linspace(0,time.time()-time_start,num = new_lenth+1)
    CS[0] = ax.contourf(X,Y,Z, 20,locator=ticker.LogLocator(), cmap= 'jet')
    print(k)

ani = animation.FuncAnimation(fig,animate,interval = 1000)
plt.show()