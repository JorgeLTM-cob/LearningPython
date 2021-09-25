# Author: Jorge Luis Torres Moreno
# Date: July 17th, 2021

import numpy as np
import pandas as pd

# Since exploring all the columns will be necessary, display options are modified
pd.set_option("display.max_rows", None, "display.max_columns", None)

# crd stands for credit record data
crd = pd.read_csv('../dataframes/credit_record.csv')

# ard stands for application record data
ard = pd.read_csv('../dataframes/application_record.csv')

# Looking if our data were properly loaded
print("DISPLAYING CREDIT RECORD:")
print(crd.head())
print(crd.tail())
print("\nDISPLAYING APPLICATION RECORD:")
print(ard.head())
print(ard.tail())

# Exploring the IDs in each dataset
print("DISPLAYING CREDIT RECORD:")
print(len(set(crd.ID)))
print("\nDISPLAYING APPLICATION RECORD:")
print(len(set(ard.ID)))
print("\nDISPLAYING SHARED IDs")
print(len(set(ard.ID).intersection(set(crd.ID))))

# Looking for null values
print(crd.info())
print(ard.info())
print(crd.isnull().sum())
print(ard.isnull().sum())

# Looking if binary columns have expected data
print("\nDISPLAYING GENDER")
print(ard.CODE_GENDER.value_counts())
print("\nDISPLAYING IF THERE IS A CAR")
print(ard.FLAG_OWN_CAR.value_counts())
print("\nDISPLAYING IF THERE IS A PROPERTY")
print(ard.FLAG_OWN_REALTY.value_counts())
print("\nDISPLAYING IF THERE IS A MOBILE")
print(ard.FLAG_MOBIL.value_counts())
print("\nDISPLAYING IF THERE IS A WORK PHONE")
print(ard.FLAG_WORK_PHONE.value_counts())
print("\nDISPLAYING IF THERE IS AN EMAIL")
print(ard.FLAG_EMAIL.value_counts())

# Looking at values in descriptive columns
print("\nDISPLAYING INCOME TYPE")
print(ard.NAME_INCOME_TYPE.value_counts())
print("\nDISPLAYING EDUCATION TYPE")
print(ard.NAME_EDUCATION_TYPE.value_counts())
print("\nDISPLAYING FAMILY STATUS")
print(ard.NAME_FAMILY_STATUS.value_counts())
print("\nDISPLAYING HOUSING TYPE")
print(ard.NAME_HOUSING_TYPE.value_counts())
print("\nDISPLAYING OCCUPATION TYPE")
print(ard.OCCUPATION_TYPE.value_counts(dropna=False))

# Looking at the descriptive statistics about numerical data
print("\nDISPLAYING NUMBER OF CHILDREN")
print(ard.CNT_CHILDREN.describe())
print("\nDISPLAYING INCOME")
print(ard.AMT_INCOME_TOTAL.describe())
print("\nDISPLAYING DAYS BIRTH")
print(ard.DAYS_BIRTH.describe())
print("\nDISPLAYING DAYS EMPLOYED")
print(ard.DAYS_EMPLOYED.describe())
print("\nDISPLAYING NUMBER OF FAMILY MEMBERS")
print(ard.CNT_FAM_MEMBERS.describe())

# Looking for outliers
print("\nDISPLAYING NUMBER OF CHILDREN")
print(ard.CNT_CHILDREN.loc[ard.CNT_CHILDREN > 1].value_counts())
print("\nDISPLAYING DAYS EMPLOYED")
print(ard.DAYS_EMPLOYED.loc[(ard.DAYS_EMPLOYED >= 0) & (ard.OCCUPATION_TYPE.isnull())].describe())
print("\nDISPLAYING FAMILY MEMBERS")
print(ard.CNT_FAM_MEMBERS.loc[ard.CNT_FAM_MEMBERS > 3].value_counts())
print("\nDISPLAYING DAYS EMPLOYED")
print(ard.loc[ard.DAYS_EMPLOYED == 365243].head())
print(ard.loc[ard.DAYS_EMPLOYED == 365243].tail())
print(ard.NAME_INCOME_TYPE.loc[ard.DAYS_EMPLOYED == 365243].value_counts())

# Filling the null values
ard.loc[((ard.DAYS_EMPLOYED >= 0) & (ard.OCCUPATION_TYPE.isnull())), 'OCCUPATION_TYPE'] = 'Retired'
ard.OCCUPATION_TYPE.fillna('Other', inplace = True)

# Looking for duplicates
print(ard.loc[ard.duplicated()])
print(crd.loc[crd.duplicated()])

# Saving changes
ard.to_csv('../dataframes/application_record_data.csv')




