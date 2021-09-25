import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib

ListaEmpleados = pd.read_csv['empleados.csv']
select = ListaEmpleados[['TotalAtaque']]

media = select.mean()[0]
desvStd = np.std(select)[0]
mediana = np.median(select)
varianza = np.var(select)[0]

sd = select.as_matrix()
#histograma de distribucion normal
cuenta, cajas, ignorar = plt.hist(sd,20)

#Trazo de la media y de la desviacion estandar
plt.axvline(media, color = 'b')
plt.axvline(media - desvStd, color = 'r')
plt.axvline(media + desvStd, color = 'r')

plt.show()


