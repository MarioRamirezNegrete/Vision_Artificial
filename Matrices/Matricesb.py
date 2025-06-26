import numpy as np
import matplotlib.pyplot as plt

total_arrays=[] #Creamos matriz vacia

def generateMainArray(): 
    for i in range(1,6):
        array = np.random.randint(low=0, high=255, size=(3, 3)) #Creamos una matriz de 3x3 con valores random entre 0 y 255

        generateSecondaryArrays(array) #Llamamos nuestra segúnda función pasandole como parametro nuestro arreglo de 3x3 
        total_arrays.append(array) #LLamamos a append para agregar la matriz originañ reción creada a nuestra matriz vacia

        for item in generateSecondaryArrays(array): #Hacemos un ciclo que itere dobre cada devolucion de la función generateSecondaryArray
            total_arrays.append(item) #Asignamos el valor devuelto por generateSecundaryArray a nuestra matriz para guardarlo como elementos de fila

    generateFigures() #LLammos función para mostrar imagenes de cada matriz en escala de grises
    
def generateSecondaryArrays(array):
    inner_arrays=[] #Creamos una matriz vacia
    for i in range(2,6):
        secondaryArrays = np.repeat(np.repeat(array, i, axis=0), i, axis=1) #Expadimos la matriz de nuestro array i veces en fila y columnas
        inner_arrays.append(secondaryArrays) #Añadimos a la matriz nuestro array expandido

    return inner_arrays # #devolvemos un array de una fila con 4 columnas
    
def generateFigures():

    fg = plt.figure(figsize=(10,10))

    for i in range(len(total_arrays)):
        sub = fg.add_subplot(5, 5, i + 1) #
        print(total_arrays[i]) #
        sub.imshow(total_arrays[i], cmap='gray') #
        
    plt.show()
 
generateMainArray()

