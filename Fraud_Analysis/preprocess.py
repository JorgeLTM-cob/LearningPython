# Author: Jorge Luis Torres Moreno
# Date: July 14th, 2021

import pandas as pd
import numpy as np

# Since exploring all the columns will be necessary, display options are modified
pd.set_option("display.max_rows", None, "display.max_columns", None)

# ccd stands for credit card data
ccd = pd.read_csv('credit_card.csv', index_col = 0)

# Knowing our data
print(ccd.head())
print(ccd.tail())
print(ccd.info())
print(ccd.isnull().sum())

# Looking for missing values
# Tip: display one item by time
print(ccd.loc[ccd.activated_date.isnull()])
print(ccd.loc[ccd.last_payment_date.isnull()])
print(ccd.loc[ccd.balance.isnull()])
print(ccd.loc[ccd.cash_advance.isnull()])
print(ccd.loc[ccd.prc_full_payment.isnull()])
print(ccd.loc[ccd.credit_limit.isnull()])

# Filling the Null values
# Using the date of the previous row to fill missing value
ccd.activated_date.fillna(method = 'ffill', inplace = True)

# Using activated_date to fill missing values in last_payment_date 
# only if a payment or an advance_cashed has happened 
ccd.loc[(ccd.last_payment_date.isnull()) & ((ccd.cash_advance > 0) | (ccd.payments > 0)), 'last_payment_date'] = ccd.activated_date

# Filling values with the corresponding medians
a = ccd.balance.median()
ccd.balance.fillna(a, inplace = True)
b = ccd.prc_full_payment.median()
ccd.prc_full_payment.fillna(b, inplace = True)
c = ccd.credit_limit.median()
ccd.credit_limit.fillna(c, inplace = True)
d = ccd.minimum_payments.median()
ccd.minimum_payments.fillna(d, inplace = True)

# Filling cash_advance's missing values with its median
# only if cash_advance_frequency is greater than 0
b = ccd.cash_advance.loc[ccd.cash_advance_frequency > 0.0].median() 
ccd.loc[(ccd.cash_advance.isnull()) & (ccd.cash_advance_frequency > 0.0), 'cash_advance'] = b
# Filling with cero the rest of the missing values
ccd.cash_advance.fillna(0.0, inplace = True)

#Looking for outliers
print(ccd.describe())

# Looking for duplicates
print(ccd.loc[ccd.duplicated()])

# Saving the cleaned data to a new csv in order to use it for the analysis
ccd.to_csv('new_credit_card.csv')
