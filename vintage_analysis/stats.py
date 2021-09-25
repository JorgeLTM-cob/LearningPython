# Author: Jorge Luis Torres Moreno
# Date: July 15th, 2021

import numpy as np
import pandas as pd

# Loading data
ard = pd.read_csv('../dataframes/application_record_data.csv')
print("\nINCOME BY GROUP")
print(ard.AMT_INCOME_TOTAL.groupby(ard.NAME_INCOME_TYPE).describe())
print("\nINCOME BY EDUCATION TYPE")
print(ard.AMT_INCOME_TOTAL.groupby(ard.NAME_EDUCATION_TYPE).describe())
print("\nINCOME BY FAMILY STATUS")
print(ard.AMT_INCOME_TOTAL.groupby(ard.NAME_FAMILY_STATUS).describe())
print("\nINCOME BY HOUSING TYPE")
print(ard.AMT_INCOME_TOTAL.groupby(ard.NAME_HOUSING_TYPE).describe())
print("\nINCOME BY OCCUPATION TYPE")
print(ard.AMT_INCOME_TOTAL.groupby(ard.OCCUPATION_TYPE).describe())
print("\nINCOME BY NUMBER OF CHILDREN")
print(ard.AMT_INCOME_TOTAL.groupby(ard.CNT_CHILDREN).describe())
