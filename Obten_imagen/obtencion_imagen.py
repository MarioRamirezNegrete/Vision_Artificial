import cv2
import matplotlib.pyplot as plt
import numpy as np

camara = cv2.VideoCapture(0)
ret, frame = camara.read(0)

if ret:
    cv2.imwrite('prueba.jpg',frame)
    print('imagen guardada')
else:
    print('Error de camara')

camara.release()
cv2.destroyAllWindows

imagen =cv2.imread('prueba.jpg')
R = imagen [:,:,2]
G = imagen [:,:,1]
B = imagen [:,:,0]
imagen [:,:,2] = B
imagen [:,:,1] = G
imagen [:,:,0] = R
imagenbw = R * 0.299 + G * 0.587+ B* 0.114 
imagenbw = imagenbw.astype(np.uint8)

bordes = cv2.Canny(imagenbw,180,255)



contornos,_ = cv2.findContours(bordes,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contornos,-1, (255,255,255), 2)

plt.subplot(1,3,1)
plt.imshow(imagen)
plt.title('Imagen rgb')

plt.subplot(1,3,2)
plt.imshow(bordes,cmap='gray')
plt.title('Imagen Canny')
plt.show()