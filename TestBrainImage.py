'''
Created on May 29, 2020

@author: annam
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.signal._peak_finding import argrelextrema
from random import randint

mybins=[]
for w in range(1,255):
    mybins.append(w)
    
img= cv2.imread('BrainNoSkull.png', 0)
org_img=cv2.imread('BrainNoSkull.png', 0)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#PLOT FREQUENCIES
#ravel flattens the matrix to 1D
#hist: first arg is data, second is max number of pixel values, third is range of pixel values
#plt.hist(img.ravel(), 254, [1,254])
#plt.show()

#PROBABILITY DENSITY PLOT
#Clean data, remove black
clean_data=[]
for z in img.ravel():
    if z!=0:
        clean_data.append(z)
#displot: first arg is data, second is whether to plot a histogram, third is whether to plot a gaussian kernel density estimate
#fourth is number of bins
p=sns.distplot(clean_data,hist=True,kde=True,bins=mybins)

#FIND MINIMA
#make a list of the frequencies in the displot
l=[h.get_height() for h in p.patches]
#convert list of frequencies to numpy array
new_l=np.asarray(l)
#find maxima, order tells how may points on either side to use for the comparator (ex. greater)
#future work: calculate order so that it will work for any image
minm=argrelextrema(new_l,np.less,order=30)
#returns tuple 
#minm[k] is the array of indices of axis k of data
#convert minm on axis 0 (the only axis) to list
minm_l=minm[0].tolist()
for n in minm_l:
    #add lines to plot so I can see
    plt.axvline(x=n)
#show displot
print(minm_l)
plt.show()

#THIS IS WHERE IS GETS SKETCHY
#IMAGE MANIPULATION
#WARNING: sketchy code
#Changing to random colors
#future work: to beautify, find the maximums and make these the colors
csf=randint(25,minm_l[1])
gm=randint(minm_l[1]+1,minm_l[2])
wm=255
#height
for up in range(img.shape[0]):
    for across in range(img.shape[1]):
        selected=img[up][across]
        if selected<minm_l[1] and selected!=0:
            img[up][across]=csf 
        elif selected>minm_l[2]:
            img[up][across]=wm 
        elif selected>minm_l[1] and selected<minm_l[2]:
            img[up][across]=gm
#concatenate images horizontally
img_concat=np.concatenate((img,org_img),axis=1)
#make it look pretty
#resolution 1600x900
res=1600,900
scale_w = res[0] / img_concat.shape[1]
scale_h = res[1] / img_concat.shape[0]
scale = min(scale_w, scale_h)
width=int(img_concat.shape[1]*scale)
height=int(img_concat.shape[0]*scale)
cv2.namedWindow('Side-by-side',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Side-by-side',width,height)
cv2.imshow('Side-by-side',img_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()

    
