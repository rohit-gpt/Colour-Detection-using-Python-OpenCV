#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 22:22:17 2019

@author: rohitgupta
"""

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the image file", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# define the list of boundaries (BGR Colour Space as OpenCV represents images in reverse Numpy order)
boundaries = [
	([17, 15, 100], [50, 56, 200]), #red
	([86, 31, 4], [220, 88, 50]), #blue
	([25, 146, 190], [62, 174, 250]), #yellow
	([103, 86, 65], [145, 133, 128]) #gray
]

for (lower,upper) in boundaries:
    
    lower = np.array(lower,dtype='uint8')
    upper = np.array(upper,dtype='uint8')
    
    # find the colors within the specified boundaries and apply
	# the mask
    mask = cv2.inRange(image, lower, upper)
    
    # After calling cv2.inRange, a binary mask is returned, where 
    # white pixels (255) represent pixels that fall into the upper and lower 
    # limit range and black pixels (0) do not.
    output = cv2.bitwise_and(image, image, mask=mask)
    
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)
