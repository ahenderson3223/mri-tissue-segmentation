## MRI Brain Tissue Segmentation Project
Anna Henderson
Cornell University
Class of 2023

### Goal
To create a program that will segment an MRI images based on three tissue types--white matter, gray matter, and cerebrospinal fluid--based on the pixel intensities in 2D slices of MRI images.

### Intensity Histogram Analysis Method
The first method developed was the intensity histogram analysis method.
-The pixel intensities were put in a histogram using OpenCV.
    -Two minima were found, and the pixels were segmented into three intervals: 0 to first minimum, first minimum to second, second minimum to 255. The image was then recolored in the

[About](./AboutTheProject.md)
