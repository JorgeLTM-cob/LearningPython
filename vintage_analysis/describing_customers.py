# Author: Jorge Luis Torres Moreno
# Date: July 20th, 2021

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.style.use('ggplot')

# Loading data
# scd stands for scored customers data
scd = pd.read_csv('../dataframes/scored_customers.csv')
for i in range(13):
    scd.loc[((scd.total_score > (i * 0.5)) & (scd.total_score < ((i+1) * 0.5))), 'total_score'] = (i*0.5)

# Droping the duplicated ID column
#scd.drop('aID', axis=1, inplace=True)

scd.AMT_INCOME_TOTAL /= 100000

# Printing statistical details about customer's score
print(scd.total_score.describe())

# In order to plot some figure remove the comment from it

# Good clients
d = sns.countplot(x = 'total_score', data = scd)
#g1 = sns.countplot(x = 'CNT_FAM_MEMBERS', hue= 'total_score', data = scd.loc[scd.total_score < 1.5])
#g2 = sns.countplot(x = 'OCCUPATION_TYPE', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g3 = sns.countplot(x = 'FLAG_EMAIL', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g4 = sns.countplot(x = 'FLAG_WORK_PHONE', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g5 = sns.countplot(x = 'NAME_HOUSING_TYPE', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g6 = sns.countplot(x = 'NAME_FAMILY_STATUS', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g7 = sns.countplot(x = 'NAME_EDUCATION_TYPE', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g8 = sns.countplot(x = 'NAME_INCOME_TYPE', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g9 = sns.countplot(x = 'CNT_CHILDREN', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g10 = sns.countplot(x = 'FLAG_OWN_REALTY', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g11 = sns.countplot(x = 'FLAG_OWN_CAR', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])
#g12 = sns.countplot(x = 'CODE_GENDER', hue = 'total_score', data = scd.loc[scd.total_score < 1.5])

# Bad clients
#b1 = sns.countplot(x = 'CNT_FAM_MEMBERS', hue= 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b2 = sns.countplot(x = 'OCCUPATION_TYPE', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b3 = sns.countplot(x = 'FLAG_EMAIL', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b4 = sns.countplot(x = 'FLAG_WORK_PHONE', hue = 'total_score', data = scd.loc[scd.total_score > 1=.5], palette = "Set3")
#b5 = sns.countplot(x = 'NAME_HOUSING_TYPE', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b6 = sns.countplot(x = 'NAME_FAMILY_STATUS', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b7 = sns.countplot(x = 'NAME_EDUCATION_TYPE', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b8 = sns.countplot(x = 'NAME_INCOME_TYPE', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b9 = sns.countplot(x = 'CNT_CHILDREN', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b10 = sns.countplot(x = 'FLAG_OWN_REALTY', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b11 = sns.countplot(x = 'FLAG_OWN_CAR', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")
#b12 = sns.countplot(x = 'CODE_GENDER', hue = 'total_score', data = scd.loc[scd.total_score >= 1.5], palette = "Set3")

#plt.scatter(scd.total_score, scd.AMT_INCOME_TOTAL)
#plt.title('Score vs Income')
#plt.xlabel('Score')
#plt.ylabel('Income (Hundreds of thousands)')

#plt.scatter(scd.DAYS_BIRTH, scd.total_score)
#plt.scatter(scd.total_score.loc[scd.DAYS_EMPLOYED <= 0], scd.DAYS_EMPLOYED.loc[scd.DAYS_EMPLOYED <= 0])
#plt.title('Score vs Days Employed')
#plt.xlabel('Score')
#plt.ylabel('Days Employed')

scd.AMT_INCOME_TOTAL *= 100000

scd.to_csv('../dataframes/scored_customers_data.csv')

plt.show()
