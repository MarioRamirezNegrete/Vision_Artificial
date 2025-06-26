import numpy as np 
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

x = np.array([[1],[2],[3]]) #matriz de cracteristicas
y = np.array([2,3.5,5.5])

#plt.scatter(x,y)
#plt.show()

modelo = linear_model.LinearRegression() # declaración
modelo.fit(x,y) # ajuste
plt.scatter(x,y)
plt.plot(x,modelo.predict(x))
plt.show()

valor = np.array([[2]])
valor2 = np.array ([[3.75]])
print(modelo.predict(valor))
print(modelo.predict(valor2))

print(mean_squared_error(y_true = y, y_pred = modelo.predict(x))) #función costo
print(r2_score(y,modelo.predict(x)))
