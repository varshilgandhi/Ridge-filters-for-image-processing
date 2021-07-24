# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 09:17:16 2021

@author: abc
"""

"""

RIDGE FILTER FOR IMAGE PROCESSING

1. MEIJERING
2. SATO
3. FRANGI
4. HESSIAN


"""

from skimage import io, feature, filters
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2

#import Ridge filters
from skimage.filters import meijering, sato, frangi, hessian

#read our images and convert into gray level 
img = io.imread("leaf.jpg")
img = rgb2gray(img)

#define all ridge filters
meijering_img = meijering(img)
sato_img = sato(img)
frangi_img = frangi(img)
hessian_img  = hessian(img)

#plot above all features
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap="gray")
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(meijering_img, cmap="gray")
ax2.title.set_text('Meijering')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(sato_img, cmap="gray")
ax3.title.set_text('Sato')
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(frangi_img, cmap="gray")
ax4.title.set_text('Frangi')
ax5 = fig.add_subplot(2,2,5)
ax5.imshow(hessian_img, cmap="gray")
ax5.title.set_text('Hessian')
plt.show()

























