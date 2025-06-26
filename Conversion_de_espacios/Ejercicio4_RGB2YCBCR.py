import matplotlib.pyplot as plt
import cv2
import numpy as np

#bgr
imagen = cv2.imread("C:/Users/mario/Downloads/rick.jpg") # cargamos la imagen
imagen = cv2.resize(imagen, (200,200)) #Redimensionamos
imagendos = cv2.imread("C:/Users/mario/Downloads/ojos.png")
imagendos = cv2.resize(imagendos, (200,200))

#Obtenemos las matrices de R, G y B y las asignamos a una matriz individual
R = imagen [:,:,2]
G = imagen [:,:,1]
B = imagen [:,:,0]

R1 = imagendos [:,:,2]
G1 = imagendos [:,:,1]
B1 = imagendos [:,:,0]
#Creamos dos matrices más para transformar nuestras imagen de GBR A RGB
imagenRGB = np.copy(imagen) 
imagendosRGB = np.copy(imagendos)
#Transformamos la primera imagen
imagenRGB[:,:,0] = R
imagenRGB[:,:,1] = G
imagenRGB[:,:,2] = B

#Transformamos la segunda imagen
imagendosRGB[:,:,0] = R1
imagendosRGB[:,:,1] = G1
imagendosRGB[:,:,2] = B1

plt.subplot(1,4,1)
plt.imshow(imagenRGB)
plt.subplot(1,4,2)
plt.imshow(imagendosRGB)

#Combinamos los valores R, G y B de ambas imagenes
FR = R*.1+R1
FG = G*.1+G1
FB = B*.1+B1
imagenf = np.zeros_like(imagen) #Creamos un array con el mismo tamaño que la imagen
imagenf[:,:,0] = FR
imagenf[:,:,1] = FG
imagenf[:,:,2] = FB

plt.subplot(1,4,3)
plt.imshow(imagenf)

#YCBCR
imagenycbcr = np.zeros_like(imagen) #Creamos un array con el mismo tamaño que la imagen
Y = 0.299*FR+0.587*FG+0.114*FB
CB = (-0.1687*FR)-(0.3313*FG)+(0.5*FB)+128
CR = (0.5*FR)-(0.4187*FG)-(0.0813*FB)+128
imagenycbcr[:,:,0] = Y
imagenycbcr[:,:,1] = CB
imagenycbcr[:,:,2] = CR

plt.subplot(1,4,4)
plt.imshow(imagenycbcr)
plt.show()