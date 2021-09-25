# Author: Jorge Luis Torres Moreno
# Date: July 18th, 2021

import numpy as np
import pandas as pd

def calculate_rate(pcd, command):
    ccr['CUSTOMER_BEHAVIOUR'] = None
    exec(command)
    sumagg = ccr.CUSTOMER_BEHAVIOUR.groupby(ccr.ID).agg(sum)
    pcd = pd.merge(pcd, sumagg, on = 'ID', how = 'left')
    pcd.loc[(pcd.CUSTOMER_BEHAVIOUR > 1), 'CUSTOMER_BEHAVIOUR'] = 1
    rate = pcd.CUSTOMER_BEHAVIOUR.sum() / len(pcd)
    return (round(rate,5))

# Loading data
ccr = pd.read_csv('../dataframes/copied_credit_record.csv')
pcd = pd.read_csv('../dataframes/pivoted_credit_data.csv')


command = "ccr.loc[((ccr.STATUS == '0') | (ccr.STATUS == '1') | (ccr.STATUS == '2') | (ccr.STATUS == '3') |\
                   (ccr.STATUS == '4') | (ccr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"
gt1 = calculate_rate(pcd, command)

command = "ccr.loc[((ccr.STATUS == '1') | (ccr.STATUS == '2') | (ccr.STATUS == '3') |\
                   (ccr.STATUS == '4') | (ccr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"
gt30 = calculate_rate(pcd, command)

command = "ccr.loc[((ccr.STATUS == '2') | (ccr.STATUS == '3') |\
                   (ccr.STATUS == '4') | (ccr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"
gt60 = calculate_rate(pcd, command)

command = "ccr.loc[((ccr.STATUS == '3') | (ccr.STATUS == '4') | (ccr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"
gt90 = calculate_rate(pcd, command)

command = "ccr.loc[((ccr.STATUS == '4') | (ccr.STATUS == '5')), 'CUSTOMER_BEHAVIOUR'] = 1"
gt120 = calculate_rate(pcd, command)

command = "ccr.loc[(ccr.STATUS == '5'),'CUSTOMER_BEHAVIOUR'] = 1"
gt150 = calculate_rate(pcd, command)

summary_dt = pd.DataFrame({'situation' : ['past due more than   1 day',
                                          'past due more than  30 days',
                                          'past due more than  60 days',
                                          'past due more than  90 days',
                                          'past due more than 120 days',
                                          'past due more than 150 days'],
                           'bad customer ratio' : [  gt1,
                                                    gt30,
                                                    gt60,
                                                    gt90,
                                                   gt120,
                                                   gt150,
                                                  ]})
print(summary_dt)


