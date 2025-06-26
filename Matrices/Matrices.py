import numpy as np
import cv2
import matplotlib.pyplot as plt

x=0
fmatriz = np.zeros((5,5))

def matriz_al(): #funcion para generar la matriz original
   matriz_or = np.random.randint(0,255, size = (3,3))
   return matriz_or

def expand_matr ():
   print('\n\n')
   matrizexp = matriz_al()
   print(matrizexp)
   print('\n\n')
   j = 0
   x = x+1
   fmatriz[x,j] = matrizexp
   

   for i in range (2,6):
     j = j+1
     matrizf = np.repeat(np.repeat(matrizexp,i, axis =0), i, axis=1)
     print(matrizf)
     print('\n\n')
     fmatriz[x,j] = matrizexp
     #fmatriz[0,j] = 
     #plt.figure(figsize=(10,10))
     #plt.imshow(matrizf,cmap='gray',vmin = 0, vmax= 255) 
     #plt.title()
     #plt.axis('off')
     #plt.show()

   return 




for i in range (1,6):
   print('Matriz {0}----------'.format(i))

   expand_matr()

'''plt.figure(figsize=(10,10))
plt.imshow(m1,cmap='gray',vmin = 0, vmax= 255) 
plt.tittle()
plt.axis('off')
plt.show()'''
   
