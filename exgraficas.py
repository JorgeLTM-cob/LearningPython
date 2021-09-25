import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.style.use('ggplot')

tabla1 = pd.read_csv('Caliente.csv')
tabla2 = pd.read_csv('Frio.csv')

datos1 = tabla1[['millasg','desp','tiempo']]
datos2 = tabla2[['millasg','desp','tiempo']]

PromC = datos1.apply(np.mean)
PromF = datos2.apply(np.mean)

f,((ax1, ax2),(ax3, ax4)) = plt.subplots(2,2,sharey = True)

ax1.scatter(datos1.desp,datos1.millasg)
ax1.axhline(PromC.millasg, color = 'k')
ax1.axvline(PromC.desp, color = 'k')
ax1.set_title('Clima_Caliente')
ax1.set_ylabel('millas/seg')

ax2.scatter(datos1.tiempo,datos1.millasg)
ax2.axhline(PromC.millasg, color = 'k')
ax2.axvline(PromC.tiempo, color = 'k')
ax2.set_title('Clima_Caliente')

ax3.scatter(datos2.desp,datos2.millasg)
ax3.axhline(PromF.millasg, color = 'k')
ax3.axvline(PromF.desp, color = 'k')
ax3.set_title('Clima_Frio')
ax3.set_ylabel('millas/seg')
ax3.set_xlabel('desp')

ax4.scatter(datos2.tiempo,datos2.millasg)
ax4.axhline(PromF.millasg, color = 'k')
ax4.axvline(PromF.tiempo, color = 'k')
ax4.set_title('Clima_Frio')
ax4.set_xlabel('tiempo')

print(PromC.millasg)
print(PromF.millasg)
print(PromC.desp)
print(PromF.desp)
print(PromC.tiempo)
print(PromF.tiempo)


plt.show()

