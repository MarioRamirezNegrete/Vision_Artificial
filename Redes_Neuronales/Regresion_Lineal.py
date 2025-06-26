#Programa  para hacer regresión lineal
import numpy as np

def linearRegresion (x, y): # lista de elementos de x y lista de lementos de y
    mean_x = np.sum(x)/len(x)
    mean_y = np.sum(y)/len(y)
    #for i in range (len(x)):
    a1 = (np.sum((x-mean_x)*(y-mean_y)))/(np.sum((x-mean_x)**2))
    a0 = mean_y - a1*mean_x
    print(f"Ecuación de la recta: y = {a0:.2f} + {a1:.2f}x")

x = np.array([1,2,3])
y = np.array([2,3,5])
linearRegresion(x,y)