# MRI Brain Tissue Segmentation Project

A script that segments a 2D MRI brain image.

The script segments the image into three parts. Then, we will compare the resulting image's segments with the location of the three types of brain tissue: white matter, gray matter, and cerebrospinal fluid.

# Project Status

This project is in-progress. The script currently displays the segmented image alongside the original image for a pre-determined file. The project will be expanded to allow saving a file of the segmented image rather than just displaying it. We also will draw comparisons with the segments in the image and the locations of the three tissue types.

# Project Screen Shots

![screenshot](https://github.com/ahenderson3223/mri-tissue-segmentation/blob/master/Images/ScreenshotSideBySide.png?raw=true)

# Technologies used

Python libraries: OpenCV, numpy, matplotlib, seaborn, scipy

# Reflection

My interest in Computer Vision and biology inspired me to begin this project. I wanted to create something that had the potential to aid in the medical field.

Although my project is (currently) not for medical use, I was interested in what would occur if I performed image segmentation on MRI images.

# Thresholding and Intensity Histogram Analysis Method

The images is segmented using thresholding.

The frequency (# pixels) of each intensity (0-255) is plotted at a histogram using OpenCV.
A curve is then fit to this data and two minima are found, forming three intervals of the intensities:

- 0 to first minimum
- first minimum to second
- second minimum to 255

The image is then thresholded using these values with the following method:
For pixel intensity I, threshold 1 T1, threshold 2 T2:

- For I &leq; T1, recolor the pixel as T1.
- For T1 &lt; I &leq; T2, recolor pixel as T2
- For I &gt; T2, recolor pixel as 255.

This results in a segmented image, thresholded to three intensities.
