import numpy as np
import cv2

# Cargamos la imagen
original = cv2.imread("monedas2.jpg")
cv2.imshow("original", original)

# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (5, 5), 0)

cv2.imshow("suavizado", gauss)

# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 150, 200)

cv2.imshow("canny", canny)

# Buscamos los contornos
(contornos, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Mostramos el número de monedas por consola
print("Número de elementos en la imagen: {}".format(len(contornos)))

cv2.drawContours(original, contornos, -1, (0, 0, 255), 4)
cv2.imshow("contornos", original)

cv2.waitKey(0)