# Author: Jorge Luis Torres Moreno
# Date: July 18th, 2021
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Loading data
pcd = pd.read_csv('../dataframes/pivoted_credit_data.csv')
ls = []
for i in range(61):
    ratio = len(pcd.loc[pcd.window < i]) / len(set(pcd.ID))
    ls.append(ratio)
pd.Series(ls).plot(legend = False, grid = True, title = ' ')
plt.xlabel('Observed Window')
plt.ylabel('Account Ratio')
plt.show()
