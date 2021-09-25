# Author: Jorge Luis Torres Moreno
# Date: July 14th, 2021

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

# Loading data
ccd = pd.read_csv('new_credit_card.csv', index_col = 0)

# Defining parameters using Freedman-Diaconis rule
q1 = np.percentile(ccd.balance, 25)
q3 = np.percentile(ccd.balance, 75)
iqr = q3 - q1
m = ccd.balance.median()
n = len(ccd.balance)
n = n**(1/3)
bins_width = 2 * iqr / n
maximum = ccd.balance.max()
n_bins = maximum / bins_width

# Printing parameters
print(q1)
print(m)
print(q3)

# Plotting the histogram
plt.hist(ccd.balance, bins = int(n_bins))
min_ylim, max_ylim = plt.ylim()
plt.axvline(q1, color = 'k', linestyle = 'dashed')
plt.text(q1*1.2, max_ylim*0.95, 'Q1')
plt.axvline(m, color = 'k', linestyle = 'dashed')
plt.text(m*1.1, max_ylim*0.95, 'Median')
plt.axvline(q3, color = 'k', linestyle = 'dashed')
plt.text(q3*1.05, max_ylim*0.95, 'Q3')
plt.title('Balance.')
plt.xlabel('USD')
plt.ylabel('Frequency')
plt.show()
