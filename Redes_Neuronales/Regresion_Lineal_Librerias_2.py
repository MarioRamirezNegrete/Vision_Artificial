import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./brain_body.txt", delim_whitespace=True)

x = df[['Brain']]
y = df['Body']

# Fi (letra griega) significa ajustado

model = linear_model.LinearRegression()

model.fit(x,y)

plt.scatter(x,y)

plt.plot(x, model.predict(x), 'r')

plt.show()