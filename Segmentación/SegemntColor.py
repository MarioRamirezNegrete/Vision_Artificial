import matplotlib.pyplot as plt
import cv2
import numpy as np

imagen = cv2.imread("C:/Users/mario/Downloads/rick.jpg") # cargamos la imagen
imagen = cv2.resize(imagen, (200,200)) #Redimensionamos
R = imagen [:,:,2]
G = imagen [:,:,1]
B = imagen [:,:,0]

imagenRGB = np.copy(imagen) 

imagenRGB[:,:,0] = R
imagenRGB[:,:,1] = G
imagenRGB[:,:,2] = B

imagenHSV = np.copy(imagen) 
imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)

low = np.array([0,100,100])
high = np.array([10,255,255])
mascara =cv2.inRange(imagenHSV,low,high) #convolucion de mascara con la imagen

segment = cv2.bitwise_and(imagen,imagen,mask= mascara) #ELIMINAMOS TODAS LAS TONALIDADES ROJAS

plt.subplot(1,3,1)
plt.imshow(mascara,cmap='gray')
plt.title('Mascara')

plt.subplot(1,3,2)
plt.imshow(segment)
plt.title('Imagen segmentada')

segmentrgb = cv2.cvtColor(segment,cv2.COLOR_BGR2RGB)

plt.subplot(1,3,3)
plt.imshow(segmentrgb)
plt.title('Imagen segmentada RGB')
plt.show()