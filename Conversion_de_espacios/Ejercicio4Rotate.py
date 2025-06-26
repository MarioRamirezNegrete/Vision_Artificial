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

plt.subplot(1,3,1)
plt.imshow(imagenbw, cmap='gray')
plt.title('Imagen blanco y negro')


#Imagen rotada 90 grados, matriz transpuesta, filas se vuelven columnas-------------------------
imagentran = np.zeros_like(imagen) #Creamos nueva matriz vacia
m,n = np.shape(imagenbw) #Tomamos medida de nuestra matriz ooriginal en x y y
for i in range(m):
    for j in range (n):
        imagentran[i,j] = imagenbw[j,i]  #Transponemos la matriz
           

plt.subplot(1,3,2)
plt.imshow(imagentran, cmap='gray')
plt.title('Imagen transpuesta')

#Rotacion de 45 grados

# Rotación de la imagen
rotation45 = 45
# Convertir a radianes
Radianes = rotation45 * np.pi / 180.0

# Obtener dimensiones de la imagen
height, width = imagenbw.shape[:2]  # Solo tomamos height y width
num_canales = imagenbw.shape[2] if len(imagenbw.shape) == 3 else 1

# Crear una imagen de salida con el tamaño adecuado
'Eleva la altura y la anchura al cuadrado, suma esos valores'
'toma la raíz cuadrada del resultado y luego convierte el valor a un número entero.'
max_len = int(math.sqrt(height*2 + width*2))
rotated_image = np.zeros((max_len, max_len, num_canales), dtype=np.uint8)

rotated_height, rotated_width = rotated_image.shape[:2]
mid_row = (rotated_height) / 2
mid_col = (rotated_width )/ 2

# Rotación manual de la imagen
for r in range(rotated_height):
    for c in range(rotated_width):
        # Aplicar matriz de rotación inversa
        y = (r - mid_col) * math.cos(Radianes) + (c - mid_row) * math.sin(Radianes)
        x = -(r - mid_col) * math.sin(Radianes) + (c - mid_row) * math.cos(Radianes)

        # Ajustar valores
        y += mid_col
        x += mid_row

        # Redondear valores
        x = round(x)
        y = round(y)

        # Verificar si están dentro de la imagen original
        if 0 <= x < width and 0 <= y < height:
            rotated_image[r, c] = imagenbw[y, x]

# Mostrar resultados
plt.figure(figsize=(12, 4))

'''plt.subplot(1, 3, 1)
plt.plot(hist)
plt.title("Histograma de la imagen binarizada")
plt.xlabel("Valor de píxel")
plt.ylabel("Frecuencia")'''
'''
plt.subplot(1, 3, 2)
plt.title("Imagen transpuesta")
plt.imshow(entero, cmap='gray')'''

plt.subplot(1, 3, 3)
plt.imshow(rotated_image, cmap='gray')
plt.title("Imagen rotada")

plt.show()
    