'''
Created on May 29, 2020

@author: annam
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.signal._peak_finding import argrelextrema
import argparse


def parse_args():
    """Parse image argument
    """
    parser = argparse.ArgumentParser(
        description='Name of image for segmentation')
    parser.add_argument("--image", help="image",
                        default="Images/BrainNoSkull.png")
    args = parser.parse_args()
    return args.image


def display_hist(minima):
    '''Display intensity histogram with vertical lines marking each [minima] value. Print minima values.
    '''
    for n in minima:
        plt.axvline(x=n)
    print(minima)
    plt.show()


img_name = parse_args()
img = cv2.imread(img_name, 0)
org_img = cv2.imread(img_name, 0)

# flatten image, remove black (background )
flat_img = img.ravel()
clean_data = np.delete(flat_img, np.where(flat_img == 0))

# PROBABILITY DENSITY PLOT
# plot data in histogram with a gaussian kernel density estimate
p = sns.distplot(clean_data, hist=True, kde=True, bins=list(range(1, 255)))

# FIND MINIMA
frequencies = [h.get_height() for h in p.patches]
np_freq = np.asarray(frequencies)
# TODO: calculate order so that it will work for any image
minm = argrelextrema(np_freq, np.less, order=20)
minima = minm[0].tolist()

# IMAGE MANIPULATION
csf = minima[1]
gm = minima[2]-50
wm = 255
# height
for up in range(img.shape[0]):
    for across in range(img.shape[1]):
        selected = img[up][across]
        if selected < minima[1] and selected != 0:
            img[up][across] = csf
        elif selected > minima[2]:
            img[up][across] = wm
        elif selected > minima[1] and selected < minima[2]:
            img[up][across] = gm

# DISPLAY IMAGES
img_concat = np.concatenate((img, org_img), axis=1)
scale_w = 1600 / img_concat.shape[1]
scale_h = 900 / img_concat.shape[0]
scale = min(scale_w, scale_h)
width = int(img_concat.shape[1]*scale)
height = int(img_concat.shape[0]*scale)
cv2.namedWindow('Side-by-side', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Side-by-side', width, height)
cv2.imshow('Side-by-side', img_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()
