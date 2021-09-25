# Author: Jorge Luis Torres Moreno
# Date: July 20th, 2021
import numpy as np
import pandas as pd

# Loading data
scd = pd.read_csv('../dataframes/scored_customers.csv')

#Assigning numerical values to binary variables

scd.loc[(scd.CODE_GENDER == 'F'), 'CODE_GENDER'] = 1
scd.loc[(scd.CODE_GENDER == 'M'), 'CODE_GENDER'] = 0
scd.CODE_GENDER = scd.CODE_GENDER.astype(np.int8)
scd.loc[(scd.FLAG_OWN_CAR == 'Y'), 'FLAG_OWN_CAR'] = 1
scd.loc[(scd.FLAG_OWN_CAR == 'N'), 'FLAG_OWN_CAR'] = 0
scd.FLAG_OWN_CAR = scd.FLAG_OWN_CAR.astype(np.int8)
scd.loc[(scd.FLAG_OWN_REALTY == 'Y'), 'FLAG_OWN_REALTY'] = 1
scd.loc[(scd.FLAG_OWN_REALTY == 'N'), 'FLAG_OWN_REALTY'] = 0
scd.FLAG_OWN_REALTY = scd.FLAG_OWN_REALTY.astype(np.int8)


r = np.corrcoef(scd.AMT_INCOME_TOTAL, scd.total_score)[0][1]
print("ANNUAL INCOME")
print(r)
r = np.corrcoef(scd.DAYS_BIRTH.loc[scd.DAYS_BIRTH < 0], scd.total_score.loc[scd.DAYS_BIRTH < 0])[0][1]
print("DAYS BIRTH")
print(r)
r = np.corrcoef(scd.DAYS_EMPLOYED, scd.total_score)[0][1]
print("DAYS EMPPLOYED")
print(r)
r = np.corrcoef(scd.CNT_FAM_MEMBERS, scd.total_score)[0][1]
print("FAMILY MEMBERS")
print(r)
r = np.corrcoef(scd.CNT_CHILDREN, scd.total_score)[0][1]
print("NUMBER OF CHILDREN")
print(r)
r = np.corrcoef(scd.CODE_GENDER, scd.total_score)[0][1]
print("GENDER")
print(r)
r = np.corrcoef(scd.FLAG_OWN_CAR, scd.total_score)[0][1]
print("CAR")
print(r)
r = np.corrcoef(scd.FLAG_OWN_REALTY, scd.total_score)[0][1]
print("REALTY")
print(r)
r = np.corrcoef(scd.FLAG_WORK_PHONE, scd.total_score)[0][1]
print("WORK PHONE")
print(r)
r = np.corrcoef(scd.FLAG_EMAIL, scd.total_score)[0][1]
print("EMAIL")
print(r)

# Print amount of good clients
print("GOOD CLIENTS")
print(scd.total_score.loc[scd.total_score < 1.5].count())

# Print amount of bad clients
print("BAD CLIENTS")
print(scd.total_score.loc[scd.total_score >= 1.5].count())

