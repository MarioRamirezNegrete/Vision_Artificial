import numpy as np
from PIL import Image

def Ycbcr2rgb(y,cb,cr):
    cb_norm = cb - 128
    cr_norm = cr - 128
    vect_res= []
    conv = [
        [1, 0, 1.402],
        [1, -0.344136, -0.714136],
        [1, 1.772, 0]
        ]
    
    dat_ori = [y, cb_norm, cr_norm]
    
    for fila in conv:
        mult = 0
        for i in range(len(fila)):
            mult += fila[i] * dat_ori[i]
        vect_res.append(mult)
    return vect_res

imagen = Image.open("C:/Users/mario/Downloads/google.jpg")
imagen_ycbcr = imagen.convert('YCbCr') #Convertir la imagen a YCbCr
datos_ycbcr = np.array(imagen_ycbcr) # Obtener los datos de la imagen como un arreglo NumPy

# Crear un arreglo vacío para almacenar la imagen RGB
alto, ancho, _ = datos_ycbcr.shape #Guardamos ancho y alto de la imagen
datos_rgb = np.zeros((alto, ancho, 3), dtype=np.uint8)


for i in range(alto):
    for j in range(ancho):
        y, cb, cr = datos_ycbcr[i, j]  # Obtener los valores YCbCr del píxel
        r, g, b = Ycbcr2rgb(y, cb, cr)  # Convertir a RGB
        datos_rgb[i, j] = [r, g, b]  # Guardar el resultado


imagen_rgb = Image.fromarray(datos_rgb, mode='RGB') #Convertir el arreglo NumPy de vuelta a una imagen

imagen_rgb.save("C:/Users/mario/Downloads/google_rgb.jpg")  # Guarda la imagen
imagen_rgb.show()  # Muestra la imagen


