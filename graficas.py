import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.style.use('ggplot')

#PobProm = 36269430

tabla1 = pd.read_csv('Febrerogot.csv')
tabla2 = pd.read_csv('Marzogot.csv')
tabla3 = pd.read_csv('Abrilgot.csv')
tabla4 = pd.read_csv('Mayogot.csv')

datos1 = tabla1[['Dia', 'Ingreso', 'ISR', 'Ingreso_Neto']]
datos2 = tabla2[['Dia', 'Ingreso', 'ISR', 'Ingreso_Neto']]
datos3 = tabla3[['Dia', 'Ingreso', 'ISR', 'Ingreso_Neto']]
datos4 = tabla4[['Dia', 'Ingreso', 'ISR', 'Ingreso_Neto']]

VentProm1 = datos1.apply(np.mean)
VentProm2 = datos2.apply(np.mean)
VentProm3 = datos3.apply(np.mean)
VentProm4 = datos4.apply(np.mean)

f,((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2,sharey = True)


ax1.scatter(datos1.Dia,datos1.Ingreso_Neto)
ax1.axhline(VentProm1.Ingreso_Neto, color='k', linestyle='--')
ax1.set_title('Febrero')
ax1.set_ylabel('Ingresos')
ax2.scatter(datos2.Dia,datos2.Ingreso_Neto)
ax2.axhline(VentProm2.Ingreso_Neto, color='k', linestyle='--')
ax2.set_title('Marzo')
ax3.scatter(datos3.Dia,datos3.Ingreso_Neto)
ax3.axhline(VentProm3.Ingreso_Neto, color='k', linestyle='--')
ax3.set_title('Abril')
ax3.set_xlabel('Dia')
ax3.set_ylabel('Ingresos')
ax4.scatter(datos4.Dia,datos4.Ingreso_Neto)
ax4.axhline(VentProm4.Ingreso_Neto, color='k', linestyle='--')
ax4.set_title('Mayo')
ax4.set_xlabel('Dia')
plt.show()
