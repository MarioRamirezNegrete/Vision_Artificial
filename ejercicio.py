import matplotlib.pyplot as plt
import cv2
import numpy as np

walle = cv2.imread("C:/Users/mario/Downloads/walle_ruido.jpg") # cargamos la imagen
walle = cv2.resize(walle, (200,200)) #Redimensionamos
rayo = cv2.imread("C:/Users/mario/Downloads/rayo_ruido.jpg") # cargamos la imagen
rayo = cv2.resize(rayo, (200,200)) #Redimensionamos

walleR = walle [:,:,2]
walleG = walle [:,:,1]
walleB = walle [:,:,0]

walleRGB = np.copy(walle) 

walleRGB[:,:,0] = walleR
walleRGB[:,:,1] = walleG
walleRGB[:,:,2] = walleB

rayoR = rayo [:,:,2]
rayoG = rayo [:,:,1]
rayoB = rayo [:,:,0]

rayoRGB = np.copy(rayo) 

rayoRGB[:,:,0] = rayoR
rayoRGB[:,:,1] = rayoG
rayoRGB[:,:,2] = rayoB

plt.subplot(3,4,1)
plt.imshow(walleRGB)
plt.title('walle rgb')

plt.subplot(3,4,2)
plt.imshow(rayoRGB)
plt.title('rayo rgb')


#walleRGBfil = cv2.GaussianBlur(walleRGB,(5,5), 3)
walleRGBfilmed = cv2.medianBlur(walleRGB,5)
#rayoRGBfil = cv2.GaussianBlur(rayoRGB,(3,3), 3)
rayoRGBfilmed = cv2.medianBlur(rayoRGB,5)
'''
plt.subplot(2,4,3)
plt.imshow(walleRGBfil)
plt.title('WALLE fitro gauss')'''

plt.subplot(3,4,3)
plt.imshow(walleRGBfilmed)
plt.title('walle filtro med')

'''
plt.subplot(2,4,5)
plt.imshow(rayoRGBfil)
plt.title('rayo fitro gauss')'''

plt.subplot(3,4,4)
plt.imshow(rayoRGBfilmed)
plt.title('rayo filtro med')


# walleRGBfilmed[:,:,0]
# Segmento BORDES------------------------------------
#Pasamos a blanco y negro para luego umbralizar 
wallebw = walleRGBfilmed[:,:,0] * 0.299 + walleRGBfilmed[:,:,2] * 0.114 + walleRGBfilmed[:,:,1] * 0.587
walleum = wallebw.astype(np.uint8) #255

rayobw = rayoRGBfilmed[:,:,0] * 0.299 + rayoRGBfilmed[:,:,2] * 0.114 + rayoRGBfilmed[:,:,1] * 0.587
rayoum = rayobw.astype(np.uint8) #255

m,n = np.shape(walleum) # Umbralización
for i in range(m):
    for j in range (n):
        if (walleum[i,j]>140):
            walleum[i,j] = 1
        else:
            walleum[i,j] = 0

m,n = np.shape(rayoum) # Umbralización
for i in range(m):
    for j in range (n):
        if (rayoum[i,j]>100):
            rayoum[i,j] = 1
        else:
            rayoum[i,j] = 0


wallex= cv2.Sobel(walleum,cv2.CV_64F,1,0,ksize = 3)
walley= cv2.Sobel(walleum,cv2.CV_64F,0,1,ksize = 3)
wallegrad = np.sqrt((wallex**2)+ (walley**2))

rayox= cv2.Sobel(rayoum,cv2.CV_64F,1,0,ksize = 3)
rayoy= cv2.Sobel(rayoum,cv2.CV_64F,0,1,ksize = 3)
rayograd = np.sqrt((rayox**2)+ (rayoy**2))


plt.subplot(3,4,5)
plt.imshow(wallegrad,cmap='gray')
plt.title('walle segmentado bordes')

plt.subplot(3,4,6)
plt.imshow(rayograd, cmap= 'gray')
plt.title('rayo segmentado bordes')

#Segmento por color
walleHSV = np.copy(walleRGBfilmed) 
walleHSV = cv2.cvtColor(walleRGBfilmed,cv2.COLOR_RGB2HSV)

rayoHSV = np.copy(rayoRGBfilmed) 
rayoHSV = cv2.cvtColor(rayoRGBfilmed,cv2.COLOR_RGB2HSV)




#walle-----------------------------------
lownaranja = np.array([10,100,100]) #Naranja
highnarnja = np.array([25,255,255])
mascarawalle_naranja =cv2.inRange(walleHSV,lownaranja,highnarnja) #convolucion de mascara con la imagen
segmentwalle_naranja = cv2.bitwise_and(walleRGBfilmed,walleRGBfilmed,mask= mascarawalle_naranja) 

lowamarillo_walle = np.array([25,100,100]) #amarillo
highamarillo_walle= np.array([35,255,255])
mascarawalle_amarillo =cv2.inRange(walleHSV,lowamarillo_walle,highamarillo_walle) #convolucion de mascara con la imagen
segmentwalle_amarillo = cv2.bitwise_and(walleRGBfilmed,walleRGBfilmed,mask= mascarawalle_amarillo)

wallecolor = cv2.add(segmentwalle_naranja, segmentwalle_amarillo)

lowverde_walle = np.array([35,100,100]) #verde
highverde_walle = np.array([85,255,255])
mascarawalle_verde =cv2.inRange(walleHSV,lowverde_walle,highverde_walle) #convolucion de mascara con la imagen
segmentwalle_verde = cv2.bitwise_and(walleRGBfilmed,walleRGBfilmed,mask= mascarawalle_verde)
wallecolor = cv2.add(wallecolor, segmentwalle_verde)

plt.subplot(3,4,7)
plt.imshow(wallecolor)
plt.title('Walle segmentacion color')
#Rayo--------------------------------
lowrojo = np.array([170,50,50]) #Rojo altos
highrojo = np.array([180,255,255])
mascararayo_rojo =cv2.inRange(rayoHSV,lowrojo,highrojo) #convolucion de mascara con la imagen
segmentrayo_rojo = cv2.bitwise_and(rayoRGBfilmed,rayoRGBfilmed,mask= mascararayo_rojo) 

lowblanco = np.array([0,0,150]) #blanco
highblanco = np.array([179,50,255])
mascararayo_blanco =cv2.inRange(rayoHSV,lowblanco,highblanco) #convolucion de mascara con la imagen
segmentrayo_blanco = cv2.bitwise_and(rayoRGBfilmed,rayoRGBfilmed,mask= mascararayo_blanco)
rayocolor = cv2.add(segmentrayo_rojo, segmentrayo_blanco)

lowrojob = np.array([9,50,50]) #Rojo bajos
highrojob = np.array([10,255,255])
mascararayo_rojob =cv2.inRange(rayoHSV,lowrojob,highrojob) #convolucion de mascara con la imagen
segmentrayo_rojob = cv2.bitwise_and(rayoRGBfilmed,rayoRGBfilmed,mask= mascararayo_rojob) 
rayocolor = cv2.add(rayocolor, segmentrayo_rojob)

plt.subplot(3,4,8)
plt.imshow(rayocolor)
plt.title('Rayo segmentacion color')
plt.show()