import numpy as np

def sigmoide (x): #Función de activación sigmoide
    s = 1/ (1+np.exp(-x))
    return s

x = np.array([0.5,1.7,0.9])
w = np.random.rand(3)
t = 0.65
b = 1
delta_w = np.zeros(3)
alpha = 0.0001 #Debe estar entre 0 y 1

for epocas in range (700):
    h = np.dot(w,x) + b
    y = sigmoide (h)
    error = (t-y)*(y)*(1-y)
    delta_w = delta_w + (error)*(x)
    w = w + alpha*delta_w
    print (y)
print (w)