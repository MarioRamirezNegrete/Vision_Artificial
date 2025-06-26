import matplotlib.pyplot as plt
import cv2
import numpy as np



def add_gaussian_noise(image, mean=0, sigma=25):

    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch)) 
    noisy_image = np.clip(image + gauss, 0, 255).astype(np.uint8) #np.clip sobre quien lo voy a hacer, valor minimo, valor maximo, todos los valores que esten por debajo dde un valor minimo los pasa a 0, y el maximo a 255
    return noisy_image





def add_salt_and_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):

    row, col, ch = image.shape
    noisy_image = image.copy()

    # Salt (valor máximo)
    num_salt = int(salt_prob * row * col)
    salt_coords = [np.random.randint(0, i-1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1], :] = 255

    # Pepper (valor mínimo)
    num_pepper = int(pepper_prob * row * col)
    pepper_coords = [np.random.randint(0, i-1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1], :] = 0

    return noisy_image


imagen = cv2.imread("C:/Users/mario/Downloads/rick.jpg") # cargamos la imagen
imagen = cv2.resize(imagen, (200,200)) #Redimensionamos
R = imagen [:,:,2]
G = imagen [:,:,1]
B = imagen [:,:,0]

imagenRGB = np.copy(imagen) 

imagenRGB[:,:,0] = R
imagenRGB[:,:,1] = G
imagenRGB[:,:,2] = B

#imagenbw = np.zeros_like(imagen)
#imagenbw = R * 0.299 + B * 0.114 + G * 0.587

plt.subplot(3,4,1)
plt.imshow(imagenRGB) # Imagen original RGB
plt.title('Imagen')


imagenruig = add_gaussian_noise(imagenRGB,mean =0 , sigma = 55) #Imagen con ruido gaussiano
plt.subplot(3,4,2)
plt.imshow(imagenruig)
plt.title('gaussiano')


imagenruisal = add_salt_and_pepper_noise(imagenRGB,salt_prob=.1, pepper_prob=.1) #Imagen con ruido sal pimienta
plt.subplot(3,4,3)
plt.imshow(imagenruisal)
plt.title('sal pimienta')

imagenf_gauss = cv2.GaussianBlur(imagenruig,(7,7), 3) #Imagen con ruido gaussiano pero con aplicacion de filtro gaussiano
plt.subplot(3,4,4)
plt.imshow(imagenf_gauss)
plt.title('Filtro_Gauss')

imagenf_medsal = cv2.medianBlur(imagenruisal,5) #Imagen con ruido sal pimienta con filtro mediana
plt.subplot(3,4,5)
plt.imshow(imagenf_medsal)
plt.title('Filtro_Mediana')


imagenf_gaussmed = cv2.medianBlur(imagenruig,5) #Imagen con  ruido gaussiano con filtro de meadiana
plt.subplot(3,4,6)
plt.imshow(imagenf_gaussmed)
plt.title('Filtro_MedianaGauss')

imagen2ruid = add_salt_and_pepper_noise(imagenruig,salt_prob=.1, pepper_prob=.1) #Imagen con mabos ruidos 
plt.subplot(3,4,7)
plt.imshow(imagen2ruid)
plt.title('Gauss Sal Pimienta')


imagenfilg = cv2.GaussianBlur(imagen2ruid,(7,7), 3) #Imagen con ambos ruidos y filtro gaussiano
plt.subplot(3,4,8)
plt.imshow(imagenfilg)
plt.title('Gauss Sal Pimienta F:Gauss')

imagenfilgmed = cv2.medianBlur(imagenfilg,1) #Imagen con ambos ruidos y ambos filtros
plt.subplot(3,4,9)

plt.imshow(imagenfilgmed)
plt.title('Gauss Sal Pimienta F:Gauss,Med')
plt.show()