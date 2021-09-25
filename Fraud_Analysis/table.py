# Author: Jorge Luis Torres Moreno
# Date: July 14th, 2021

import numpy as np
import pandas as pd
import re

# This subroutine only returns the numbers in a string 
def getNumbers(field):
    onlynumbers = ''
    parts = re.findall(r'[0-9]+', field)
    for part in parts:
        onlynumbers += part
    return onlynumbers

# Loading data
ccd = pd.read_csv('new_credit_card.csv', index_col = 0)

# Removing all the letters from the 'cust_id' column
ccd.cust_id = ccd.cust_id.apply(getNumbers)
ccd.activated_date = pd.to_datetime(ccd.activated_date)
ccd.last_payment_date = pd.to_datetime(ccd.last_payment_date)

# Creating a new DataFrame to build the requested table
table = pd.DataFrame()
table['cust_id'] = ccd.cust_id.loc[(ccd.activated_date.dt.year == 2020) & (ccd.last_payment_date.dt.year == 2020)]
table['activated_date'] = ccd.activated_date.loc[(ccd.activated_date.dt.year == 2020) & (ccd.last_payment_date.dt.year == 2020)]
table['last_payment_date'] = ccd.last_payment_date.loc[(ccd.activated_date.dt.year == 2020) & (ccd.last_payment_date.dt.year == 2020)]
table['cash_advance'] = ccd.cash_advance.loc[(ccd.activated_date.dt.year == 2020) & (ccd.last_payment_date.dt.year == 2020)]
table['credit_limit'] = ccd.credit_limit.loc[(ccd.activated_date.dt.year == 2020) & (ccd.last_payment_date.dt.year == 2020)]
table.activated_date = table.activated_date.dt.strftime('%Y-%m')
table.last_payment_date = table.last_payment_date.dt.strftime('%Y-%m-%d')
table['cashad_as_prc_of_creditlim'] = table.cash_advance / table.credit_limit

# Saving the DataFrame as a csv
table.to_csv('table_credit_card.csv')
