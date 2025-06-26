import cv2
import matplotlib.pyplot as plt
import numpy as np



imagen =cv2.imread("C:/Users/mario/Documents/Programacion/Vision/Encontrar_contornos/monedas1.jpg")
imagenrgb = np.zeros_like(imagen)
R = imagen [:,:,2]
G = imagen [:,:,1]
B = imagen [:,:,0]

imagenrgb [:,:,2] = B
imagenrgb [:,:,1] = G
imagenrgb [:,:,0] = R

imagenbw = R * 0.299 + G * 0.587+ B* 0.114 
imagenbw = imagenbw.astype(np.uint8)

bordes = cv2.Canny(imagenbw,50,150)
bordes2 = cv2.dilate(bordes, None, iterations = 11)



contornos,_ = cv2.findContours(bordes2,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos_2 = cv2.drawContours(imagenrgb, contornos,-1, (0,255,0), 2) #
print(len(contornos))
plt.subplot(1,3,1)
plt.imshow(imagenrgb)
plt.title('Imagen rgb')

plt.subplot(1,3,2)
plt.imshow(bordes,cmap='gray')
plt.title('Imagen Canny')

plt.subplot(1,3,3)
plt.imshow(contornos_2,cmap='gray')
plt.title('Imagen contornos')
plt.show()