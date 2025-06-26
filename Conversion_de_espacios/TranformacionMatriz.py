import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
imagen = cv2.imread("C:/Users/mario/Downloads/rick.jpg") # cargamos la imagen
imagen = cv2.resize(imagen, (200,200)) #Redimensionamos
R = imagen [:,:,2]
G = imagen [:,:,1]
B = imagen [:,:,0]

imagenRGB = np.copy(imagen) 

imagenRGB[:,:,0] = R
imagenRGB[:,:,1] = G
imagenRGB[:,:,2] = B

plt.subplot(2,3,1)
plt.imshow(imagenRGB)
plt.title('Imagen original')

imagenRGBx = np.copy(imagen) 
imagenRGBt = np.copy(imagen) 

imagenRGBx = imagenRGB*4
plt.subplot(2,3,2)
plt.imshow(imagenRGBx)
plt.title('Imagen multiplicada')

imagenRGBt[:,:,0] = R+5
imagenRGBt[:,:,1] = G+5
imagenRGBt[:,:,2] = B+5

plt.subplot(2,3,3)
plt.imshow(imagenRGBt)
plt.title('Imagen sumada')

imagenHSV = np.copy(imagen) 
imagenHSV = cv2.cvtColor(imagenRGB,cv2.COLOR_RGB2HSV)
plt.subplot(2,3,4)
plt.imshow(imagenHSV)
plt.title('Imagen HSV')


imagenHSVt = np.copy(imagen) 
imagenHSVx = np.copy(imagen) 

imagenHSVx = imagenHSV*4
plt.subplot(2,3,5)
plt.imshow(imagenHSVx)
plt.title('Imagen HSV multiplicada')

imagenHSVt[:,:,0] = imagenHSV[:,:,0] + 60
imagenHSVt[:,:,1] = imagenHSV[:,:,1] + 50
imagenHSVt[:,:,2] = imagenHSV[:,:,2] + 50

plt.subplot(2,3,6)
plt.imshow(imagenHSVt)
plt.title('Imagen HSV sumada')
plt.show()
