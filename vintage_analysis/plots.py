# Author: Jorge Luis Torres Moreno
# Date: July 17th, 2021

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

# Loading data
ard = pd.read_csv('../dataframes/application_record_data.csv')
ard.loc[((ard.DAYS_EMPLOYED >= 0) & (ard.OCCUPATION_TYPE.isnull()), 'OCCUPATION_TYPE')] = 'Retired'
ard.AMT_INCOME_TOTAL /= 100000

# Defining parameters using Freedman-Diaconis rule
q1 = np.percentile(ard.AMT_INCOME_TOTAL, 25)
q2 = ard.AMT_INCOME_TOTAL.median()
q3 = np.percentile(ard.AMT_INCOME_TOTAL, 75)
iqr = q3 - q1
n = len(ard.AMT_INCOME_TOTAL)
n = n**(1/3)
bins_width = 2 * iqr / n
maximum = ard.AMT_INCOME_TOTAL.max()
minimum = ard.AMT_INCOME_TOTAL.min()
n_bins = (maximum - minimum) / bins_width

# Printing parameters
print("Q1: %f", q1)
print("Q2: %f", q2)
print("Q3: %f", q3)
#print("IQR: %f", iqr)

# Plotting income histogram
mu = ard.AMT_INCOME_TOTAL.mean()
plt.hist(ard.AMT_INCOME_TOTAL.loc[ard.AMT_INCOME_TOTAL < 7], bins = 24)
min_ylim, max_ylim = plt.ylim()
plt.axvline(mu, color = 'k')
plt.text(mu*1.1, max_ylim*0.95, 'Mean: {:.3f}'.format(mu))
plt.title('Annual Income')
plt.xlabel('MXN (Hundreds of thousands)')
plt.ylabel('Frequency')
plt.xlim(0, 7)


# Plotting children histogram
#fig, child = plt.subplots()
#N, bins, patches = child.hist(ard.CNT_CHILDREN.loc[ard.CNT_CHILDREN < 6], bins = 5)
#child.set_title('Number of children')
#child.set_ylabel('Frequency')
#patches[0].set_facecolor('k')
#for i in range(1,5):
#    patches[i].set_facecolor('b')

# Scatter plot of Income vs Days of birth
#plt.scatter(ard.DAYS_BIRTH, ard.AMT_INCOME_TOTAL)
#plt.title('Income vs Days of birthe')
#plt.xlabel('Days of birth')
#plt.ylabel('MXN (Hundreds of thousands)')

# Scatter plot of Income vs Days employed
#plt.scatter(ard.DAYS_EMPLOYED.loc[ard.DAYS_EMPLOYED < 0], ard.AMT_INCOME_TOTAL.loc[ard.DAYS_EMPLOYED < 0])
#plt.title('Income vs Days employed')
#plt.xlabel('Days employed')
#plt.ylabel('MXN (Hundreds of thousands)')

# Scatter plot of Income vs Number of family members
#plt.scatter(ard.CNT_FAM_MEMBERS, ard.AMT_INCOME_TOTAL)
#plt.title('Income vs number of family members')
#plt.xlabel('Family members')
#plt.ylabel('MXN (Hundreds of thousands)')

# Scatter plot of Income vs Number of children
#plt.scatter(ard.CNT_CHILDREN, ard.AMT_INCOME_TOTAL)
#plt.title('Income vs number of children')
#plt.xlabel('Number of children')
#plt.ylabel('MXN (Hundreds of thousands)')



plt.show()
