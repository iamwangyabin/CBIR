from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

def process_image(imgname,resultname,params="--edge-thresh 10 --peak-thresh 5"):
    if imgname[-3:] != '.pgm':
        im = Image.open(imgname).convert('L')
        im.save('tmp.pgm')
        imgname='tmp.pgm'

    cmmd=str("sift "+imgname+" --output="+resultname+" "+params)
    os.system(cmmd)
    print("process "+resultname)

def read_features_from_file(filename):
    f=np.loadtxt(filename)
    return f[:,:4],f[:,4:]

def plot_features(im,locs,circle=False):
    def draw_circle(c,r):
        t=np.arange(0,1.01,.01)*2*np.pi
        x=r*np.cos(t)+c[0]
        y=r*np.sin(t)+c[1]
        plt.plot(x,y,'b',linewidth=2)
        plt.imshow(im)
    if circle:
        for p in locs:
            draw_circle(p[:2],p[2])
    else:
        plt.plot(locs[:,0],locs[:,1],'ob')
    plt.axis('off')

process_image('timg.jpg','timg.sift',params="--edge-thresh 10 --peak-thresh 5")

os.chdir('sift')
imname='timg.jpg'
im=np.array(Image.open(imname).convert('L'))

l1,l2=read_features_from_file('timg.sift')
plt.figure()
plt.gray()
plot_features(im,l1,circle=True)
plt.show()