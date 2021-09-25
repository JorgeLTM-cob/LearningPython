# Author: Jorge Luis Torres Moreno
# Date: July 18th, 2021

import numpy as np
import pandas as pd
pd.set_option("display.max_rows", 10, "display.max_columns", None)

# The explanation of why 20 was chosen is find in report.pdf
window_limit = 20

# Loading data
crd = pd.read_csv('../dataframes/credit_record.csv')

# Assigning numerical values to 'STATUS' column
crd['score'] = 0.0
crd.loc[(crd.STATUS == '5'), 'score'] = 6
crd.loc[(crd.STATUS == '4'), 'score'] = 5
crd.loc[(crd.STATUS == '3'), 'score'] = 4
crd.loc[(crd.STATUS == '2'), 'score'] = 3
crd.loc[(crd.STATUS == '1'), 'score'] = 2
crd.loc[(crd.STATUS == '0'), 'score'] = 1

# gcd stands for grouped credit data
gcd = crd.groupby('ID')

# Creating a DataFrame which shows the behaviour of an ID per row
# pcd stands for pivoted credit data
pcd = crd.pivot(index = 'ID', columns = 'MONTHS_BALANCE', values = 'STATUS')

# Finding when the credit was recieved
# Since the months are counted using negative numbers, the oldest month is also the one with
# the lowest value
pcd['start'] = gcd.MONTHS_BALANCE.min()

# Finding when the credit period finished
# Now it is necessary to find the greatest value
pcd['end'] = gcd.MONTHS_BALANCE.max()
pcd['total_score'] = gcd.score.sum()

pcd['ID'] = pcd.index

# Dropping unnecessary information
pcd = pcd[['ID','start','end', 'total_score']]

# Computing the observed window
pcd['window'] = pcd.end - pcd.start

# Change the index from using ID to consecutive indices (0, 1, 2, ..., n) to save memory
pcd.reset_index(drop = True, inplace = True)

# Joining the information
crd = pd.merge(crd, pcd, on = ['ID'], how = 'left')

# ccr stands for copy of credit record
ccr = crd.copy()

# Droppping those applicants with a small record
crd = crd.loc[crd.window > window_limit]

# Labeling customers (1: overdue, 0: ok)
crd['CUSTOMER_BEHAVIOUR'] = np.where(((crd.STATUS == '2') | (crd.STATUS == '3') | (crd.STATUS == '4') | (crd.STATUS == '5')), 1, 0)
crd.CUSTOMER_BEHAVIOUR = crd.CUSTOMER_BEHAVIOUR.astype(np.int8)

# Computing month on book, i.e.: number of months after opening an account
crd['MONTH_ON_BOOK'] = crd.MONTHS_BALANCE - crd.start
crd.sort_values(by = ['ID', 'MONTH_ON_BOOK'], inplace = True)

# csm stands for customers per starting month
csm = pcd.groupby(['start']).agg({'ID' : ['count']})
csm.reset_index(inplace = True)
csm.columns = ['start', 'number_of_clients']

# Building the "vintage table"
vintage = crd.groupby(['start', 'MONTH_ON_BOOK']).agg({'ID' : ['count']})
vintage.reset_index(inplace = True)
vintage.columns = ['start','month_on_book','number_of_clients']
vintage['due_count'] = np.nan
vintage = vintage[['start','month_on_book','due_count']]
vintage = pd.merge(vintage, csm, on = ['start'], how = 'left')

for i in range(-60, 1):
    ls = []
    for j in range(61):
        due = list(crd.ID.loc[(crd.CUSTOMER_BEHAVIOUR == 1) & (crd.MONTH_ON_BOOK == j) & (crd.start == i)])
        ls.extend(due)
        vintage.loc[(vintage.month_on_book == j) & (vintage.start == i), 'due_count'] = len(set(ls))

vintage['clients_rate'] = vintage.due_count / vintage.number_of_clients

# Creating the Standard vintage table
# svt stands for standard vintage table
svt = vintage.pivot(index = ['start'], columns = 'month_on_book', values = 'clients_rate')

# Scoring clients
crd.total_score /= crd.window 

# Saving useful DataFrames
svt.to_csv('../dataframes/standard_vintage_table.csv')
pcd.to_csv('../dataframes/pivoted_credit_data.csv')
crd.to_csv('../dataframes/new_credit_record.csv')
ccr.to_csv('../dataframes/copied_credit_record.csv')

