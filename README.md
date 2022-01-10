# MRI Brain Tissue Segmentation Project

A program that will to segment an MRI image based on three tissue types --white matter, gray matter, and cerebrospinal fluid-- based on the pixel intensities in 2D slices of MRI images.

# Project Status

# Project Screen Shots

# Installation and Setup Instructions

# Reflection

# Intensity Histogram Analysis Method

The frequency (# pixels) of each intensity (0-255) is plotted using OpenCV.
A curve is then fit to this data and two minima are found, forming three intervals of the intensities:

- 0 to first minimum
- first minimum to second
- second minimum to 255

The image is then thresholded using these values with the following method:
For pixel intensity I, threshold 1 T1, threshold 2 T2:

- For I &leq; T1, recolor the pixel as T1.
- For T1 &lt; I &leq; T2, recolor pixel as T2
- For I &gt; T2, recolor pixel as 255.

This results in a segmented image of three pixel intensities.
