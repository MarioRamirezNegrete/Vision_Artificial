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

imagenbw = np.zeros_like(imagen)
imagenbw = R * 0.299 + B * 0.114 + G * 0.587


plt.subplot(1,4,1)
plt.imshow(imagenbw, cmap='gray')
plt.title('Imagen gray')

print(np.max(imagenbw)) #280.5
imagenbw = imagenbw.astype(np.uint8) #255


hist = cv2.calcHist([imagenbw],[0],None,[255],[0,255]) #Histograma con cv2
#hist,_ = np.histogram(imagenbw,bins=256,range=(0,255)) #Histograma con numpy

#plt.plot(hist)



m,n = np.shape(imagenbw) # Umbralización
for i in range(m):
    for j in range (n):
        if (imagenbw[i,j]>210):
            imagenbw[i,j] = 1
        else:
            imagenbw[i,j] = 0


plt.subplot(1,4,2)
plt.imshow(imagenbw, cmap='gray')
plt.title('Imagen umbralizada')


sobelx= cv2.Sobel(imagenbw,cv2.CV_64F,1,0,ksize = 3)
sobely= cv2.Sobel(imagenbw,cv2.CV_64F,0,1,ksize = 3)
grad = np.sqrt((sobelx**2)+ (sobely**2))

plt.subplot(1,4,3)
plt.imshow(grad, cmap='gray')
plt.title('Imagen umbralizada sobel')
plt.show()