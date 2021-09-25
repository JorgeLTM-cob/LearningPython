# Author: Jorge Luis Torres Moreno
# Date: July 18th, 2021

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Loading data
svt = pd.read_csv('../dataframes/standard_vintage_table.csv', index_col = 0)
plt.rcParams['figure.facecolor'] = 'white'
svt.iloc[0:61].T.plot(legend = False, grid = True, title = 'Cumulative % of Bad Customer (More than 60 Days Past Due)')
plt.xlabel('Months on Books')
plt.ylabel('Cumulative % > 60 Days Past Due')
plt.xlim(0, 60)
plt.ylim(0, 0.05)
plt.show()
