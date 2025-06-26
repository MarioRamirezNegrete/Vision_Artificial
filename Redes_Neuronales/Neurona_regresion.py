import numpy as np
import matplotlib.pyplot as plt
#librerias para RNA
from keras import backend
from keras.models import Secuential
from keras.layers import Dense
from keras import optimizers
x = np.array ([[1],[2],[3]])
y = np.array ([2,3.5,5.5])

#limpiar sesión
backend.clear_session()
#crear modelo
modelo = Secuential()
modelo.add(Dense(1,use_bias=True,activation = 'linear',input_shape =(1,)))

adam = optimizers.Adam(learning_rate = 0.01, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay = 0)
modelo.compile(loss = 'mean_squared_error', optimizer = adam, metrics =['accuracy'])
modelo.fit(x,y, epoch = 200, verbose =0, validation_data =(x,y))
modelo.summary()#indica las capas del modelo
score = modelo.evaluate(x,y, verbose = 0)
print(score)
print(modelo.get_weights()[0])
print(modelo.get_weights()[1])

