# Author: Jorge Luis Torres Moreno
# Date: July 18th, 2021

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Function that computes the observed window
def observed_wdw(ncr, command):
    id_sum = len(set(pcd.ID))
    ncr.CUSTOMER_BEHAVIOUR = 0
    exec(command)
    ncr.MONTH_ON_BOOK = ncr.MONTHS_BALANCE - ncr.start
    minagg = ncr.MONTH_ON_BOOK.loc[ncr.CUSTOMER_BEHAVIOUR == 1].groupby(ncr.ID).min()
    minagg = pd.DataFrame(minagg)
    minagg['ID'] = minagg.index
    obslst = pd.DataFrame({'MONTH_ON_BOOK' : range(61), 'rate' : None})
    ls = []
    for i in range(61):
        due = list(minagg.ID.loc[minagg.MONTH_ON_BOOK == i])
        ls.extend(due)
        obslst.loc[obslst.MONTH_ON_BOOK == i, 'rate'] = len(set(ls)) / id_sum
    return (obslst.rate)

# ncr stands for new credit record
ncr = pd.read_csv('../dataframes/new_credit_record.csv', index_col=0)

pcd = pd.read_csv('../dataframes/pivoted_credit_data.csv')

command = "ncr.loc[((ncr.STATUS == '0') | (ncr.STATUS == '1') | (ncr.STATUS == '2') | (ncr.STATUS == '3') |\
                   (ncr.STATUS == '4') | (ncr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"

# gti stands for greater than i 
gt1 = observed_wdw(ncr, command)

command = "ncr.loc[((ncr.STATUS == '1') | (ncr.STATUS == '2') | (ncr.STATUS == '3') |\
                   (ncr.STATUS == '4') | (ncr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"
gt30 = observed_wdw(ncr, command)

command = "ncr.loc[((ncr.STATUS == '2') | (ncr.STATUS == '3') |\
                   (ncr.STATUS == '4') | (ncr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"
gt60 = observed_wdw(ncr, command)

command = "ncr.loc[((ncr.STATUS == '3') | (ncr.STATUS == '4') | (ncr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"
gt90 = observed_wdw(ncr, command)

command = "ncr.loc[((ncr.STATUS == '4') | (ncr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"
gt120 = observed_wdw(ncr, command)

command = "ncr.loc[(ncr.STATUS == '5'), 'CUSTOMER_BEHAVIOUR'] = 1"
gt150 = observed_wdw(ncr, command)

obslst = pd.DataFrame({'past due more than 30 days' : gt30,
                       'past due more than 60 days' : gt60,
                       'past due more than 90 days' : gt90,
                       'past due more than 120 days' : gt120,
                       'past due more than 150 days' : gt150,
                      })
obslst.plot(grid = True, title = 'Cumulative % of Bad Customers Analysis')
plt.xlabel('Months on Books')
plt.ylabel('Cumulative %')

plt.show()

