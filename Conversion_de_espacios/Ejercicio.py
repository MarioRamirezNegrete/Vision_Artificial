import matplotlib.pyplot as plt
import cv2
import numpy as np
#bgr
imagen = cv2.imread("C:/Users/mario/Downloads/rick.jpg") # cargamos la imagen

#plt.imshow(imagen)
imagen2 = np.copy(imagen)
imagen3 = np.copy(imagen)
plt.subplot(1,7,1)
plt.imshow(imagen)
R = imagen [:,:,2]
G = imagen [:,:,1]
B = imagen [:,:,0]

plt.subplot(1,7,2)
plt.imshow(R)
plt.subplot(1,7,3)
plt.imshow(G)
plt.subplot(1,7,4)
plt.imshow(B)


#RGB ------------------------------------------------

imagen2[:,:,0] = R
imagen2[:,:,1] = G
imagen2[:,:,2] = B

plt.subplot(1,7,5)
plt.imshow(imagen2)

#RGB MODIFICADO------------------------------------------
imagen2[:,:,0] = R*3
imagen2[:,:,1] = G*5
imagen2[:,:,2] = B*100


plt.subplot(1,7,6)
plt.imshow(imagen3, )

#Escala de grises
a1 = (0.299*R)
a2 = (0.587*G)
a3 =(0.114*B)
at = a1+a2+a3


plt.subplot(1,7,7)
plt.imshow(at,cmap='gray')
plt.show()