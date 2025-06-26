#Primer neurona artificial
import numpy as np

def escalon (x):
    if x > 0:
        return 1
    else:
        return 0
#OR
inputs = np.array([[0,0],[0,1],[1,0],[1,1]]) #Entradas
#targets = np.array([0,1,1,1]) #Valores deseados OR
targets = np.array([0,0,0,1]) #Valores AND
weight =  np.array([2,2]) #Peso 
bias = -3
output = []

for i in range (targets.shape[0]):
    h = np.dot(inputs[i],weight) + bias #Producto punto 
    y = escalon(h)
    output.append([h,y]) # Añadimos a nuestra matriz output el valor de h y el valor y corrrespondiente

#Imprimimos una tabla coon nuestros resultados 
print('Input','Input2','Target','Comb_Lineal','Output')
for i in range(4):
    print('', inputs[i][0],'     ',inputs[i][1],'   ',targets[i],'     ',output[i][0],'    ',output[i][1])