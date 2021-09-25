# Author: Jorge Luis Torres Moreno
# Date: July 14th, 2021

import numpy as np
import pandas as pd

# Loading data
ccd = pd.read_csv('new_credit_card.csv', index_col = 0)

# Giving the corresponding format
ccd.activated_date = pd.to_datetime(ccd.activated_date)

# Creaating a new DataFrame to show the requested data
stats = pd.DataFrame()
stats['mean_balance'] = ccd.balance.groupby([ccd.activated_date.dt.year, ccd.activated_date.dt.month]).mean()
stats['median_balance'] = ccd.balance.groupby([ccd.activated_date.dt.year, ccd.activated_date.dt.month]).median()

print(stats)
