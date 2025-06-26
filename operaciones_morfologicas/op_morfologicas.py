import matplotlib.pyplot as plt
import cv2
import numpy as np

imagen = cv2.imread("C:/Users/mario/Downloads/rick.jpg") 
R = imagen [:,:,2]
G = imagen [:,:,1]
B = imagen [:,:,0]
imagen_col = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
imagenbw = np.zeros_like(imagen)
imagenbw = R * 0.299 + G * 0.587+ B* 0.114 
imagenbw = imagenbw.astype(np.uint8)
imagen_canny = cv2.Canny(imagenbw,100,255)

plt.subplot(3,3,1)
plt.imshow(imagen_canny,cmap='gray')
plt.title('Imagen canny')
kernel = np.ones((3,3),np.uint8) #Que tanto se ensanchará
imagen_dilate = cv2.dilate(imagen_canny, kernel = kernel, iterations = 1)

plt.subplot(3,3,2)
plt.imshow(imagen_dilate,cmap='gray')
plt.title('Imagen dilatada')

imagen_erode = cv2.erode(imagen_dilate, kernel = kernel, iterations = 1)
plt.subplot(3,3,3)
plt.imshow (imagen_erode,cmap='gray')
plt.title('Imagen erosion')

imagen_dilate2 = cv2.dilate(imagen_erode,kernel = kernel, iterations=1)
plt.subplot(3,3,4)
plt.imshow(imagen_dilate2,cmap='gray')
plt.title('Imagen dilatada')

imagen_coldilate = cv2.dilate(imagen_col, kernel =kernel, iterations=8)
plt.subplot(3,3,5)
plt.imshow(imagen_coldilate)
plt.title('Imagen color dilatada')

imagen_colerode= cv2.erode(imagen_col, kernel =kernel, iterations=8)
plt.subplot(3,3,6)
plt.imshow(imagen_colerode)
plt.title('Imagen color erosion')

imagenHSV = np.copy(imagen) 
imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)

low =np.array([25,100,100])
high = np.array([35,255,255])
mascara = cv2.inRange(imagenHSV,low,high)
mascara_dilate = cv2.dilate(mascara, kernel=kernel, iterations = 15)
segment_dilate = cv2.bitwise_and(imagen_col,imagen_col,mask= mascara_dilate) 
plt.subplot(3,3,7)
plt.imshow(segment_dilate)
plt.title('Segmentación')
plt.show()
