# What is Numpy?
"""
https://numpy.org/doc/
"""
import numpy as np

n = np.arange(27)

print(n)

n = n.reshape(3,9)

print(n)

n = n.reshape(3,3,3)

print(n)

m = np.asarray([[123,12,123,12,33],[0,0,0,0,0],[0,0,0,0,0]])

print(m)

# Convert Images to Numpy Arrays

import cv2

im_g = cv2.imread("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_14/smallgray.png",0)

print(im_g)

im_g2 = cv2.imread("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_14/smallgray.png",1)

cv2.imwrite("newsmall.png",im_g2)

# Indexing, Slicing and Iterating Nympy Arrays

a = [1,2,3]

print(a[0:2])

print(im_g[0:2,2:4])

for i in im_g:
    print(i)

# Stacking and Splitting Numpy Arrays

ims = np.hstack((im_g,im_g))
print(ims)

ims2 = np.vstack((im_g,im_g))
print(ims2)

# Check vsplit and hsplit method to split numpuy arrays.