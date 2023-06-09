# -*- coding: utf-8 -*-
"""Operaciones.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VqYlwNJJvk6P3uJkKvS5MlWzO0rAB3kx
"""

import numpy as np
import pandas as pd
import cv2 as cv 
from google.colab.patches import cv2_imshow # for image display
from skimage import io
from PIL import Image 
import matplotlib.pylab as plt
import imageio
from scipy.signal import convolve2d

from google.colab import drive
drive.mount('/content/drive')

img1 = cv.imread('/content/drive/MyDrive/Maestría en Ciencias de la Computación/Visión Computacional/lion.jpg')
img2 = cv.imread('/content/drive/MyDrive/Maestría en Ciencias de la Computación/Visión Computacional/noche.jpg')

if img1.shape != img2.shape:
    img2 = cv.resize(img2, img1.shape[1::-1])

# Sumar las imágenes
sum_img = cv.add(img1, img2)

# Mostrar las imágenes y la imagen resultante
final_frame = cv.hconcat((img1, img2))
cv2_imshow(final_frame)
cv2_imshow(sum_img)

if img1.shape != img2.shape:
    img2 = cv.resize(img2, img1.shape[1::-1])

# Restar las imágenes
diff_img = cv.subtract(img1, img2)
final_frame = cv.hconcat((img1, img2))
cv2_imshow(final_frame)
cv2_imshow(diff_img)

if img1.shape != img2.shape:
    img2 = cv.resize(img2, img1.shape[1::-1])

# Promedio de las imágenes
avg_img = cv.add(img1, img2)/2

# Mostrar las imágenes y la imagen resultante
final_frame = cv.hconcat((img1, img2))
cv2_imshow(final_frame)
cv2_imshow(avg_img)

if img1.shape != img2.shape:
    img2 = cv.resize(img2, img1.shape[1::-1])

# Mutiplicar por valor una imagen
mult_img = np.multiply(img2, (1 - 0.25))
mult_img = np.array(mult_img, dtype=np.uint8)

avg_pond_img = cv.add(img1, mult_img)

# Mostrar las imágenes y la imagen resultante
final_frame = cv.hconcat((img1, img2))
cv2_imshow(final_frame)
cv2_imshow(avg_pond_img)

if img1.shape != img2.shape:
    img2 = cv.resize(img2, img1.shape[1::-1])

# Multiplicar las imágenes
mult_img = np.multiply(img1, img2)
mult_img = np.array(mult_img, dtype=np.uint8)

# Mostrar las imágenes y la imagen resultante
final_frame = cv.hconcat((img1, img2))
cv2_imshow(final_frame)
cv2_imshow(mult_img)

if img1.shape != img2.shape:
    img2 = cv.resize(img2, img1.shape[1::-1])

# Dividir las imágenes
div_img  = np.divide(img1, img2)
div_img  = np.array(div_img , dtype=np.uint8)

# Mostrar las imágenes y la imagen resultante
final_frame = cv.hconcat((img1, img2))
cv2_imshow(final_frame)
cv2_imshow(div_img )