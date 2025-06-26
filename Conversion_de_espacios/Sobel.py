import matplotlib.pyplot as plt
import cv2
import numpy as np

imagen = cv2.imread("C:/Users/mario/Downloads/rick.jpg") # cargamos la imagen
imagen = cv2.resize(imagen, (200,200)) #Redimensionamos

imagenbn = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
sx = cv2.Sobel(imagenbn,cv2.CV_64F,1,0,ksize = 3)
sy = cv2.Sobel(imagenbn,cv2.CV_64F,0,1,ksize = 3)


plt.subplot(1,4,1)
plt.imshow(imagen)
plt.title('Imagen')

plt.subplot(1,4,2)
plt.imshow(imagenbn,cmap='gray')
plt.title('Imagen blanco y negro')

plt.subplot(1,4,3)
plt.imshow(sx,cmap='gray')
plt.title('Sobelx')

plt.subplot(1,4,4)
plt.imshow(sy,cmap='gray')
plt.title('Sobel y')
plt.show()

#Gradiente
grad = np.sqrt((sx**2)+ (sy**2))
plt.plot(grad) #Grafico de gradiente}
plt.show()
plt.imshow(grad, cmap= 'gray') #Imagen del gradiente
plt.show()

#Inversa
invgrad = 1/grad
plt.imshow(invgrad, cmap= 'gray') #Inverso de gradiente
plt.show()

#restar 255-valor de la imagen
gradneg = 255 - grad
plt.imshow(gradneg,cmap='gray') #Grafico de gradiente}
plt.show()