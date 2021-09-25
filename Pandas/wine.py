import pandas as pd
import numpy as np

reviews = pd.read_csv("wines.csv", index_col = 0)
#print(reviews.country)
#print(reviews.iloc[0])
#print(reviews.iloc[:,0])
#print(reviews.iloc[:3, 0])
#print(reviews.iloc[1:3, 0])
#print(reviews.iloc[[0,1,2], 0])
#print(reviews.iloc[-5:])
#print(reviews.loc[0, 'country'])
#print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])
#
#Note: iloc works like an usual index in Python so using iloc[0:1000] will return 1000 lines.
#Whereas loc[0:1000] will return 1001 lines. Be aware!
#
#print(reviews.set_index("title"))
#print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])
#print(reviews.loc[reviews.country.isin(['Italy', 'France'])])
#print(reviews.loc[reviews.price.notnull()])
#reviews['critic'] = 'everyone' this creates a new column
#print(reviews.loc['critic'])
reviews['index_backwards'] = range(len(reviews), 0, -1)
print(reviews.index_backwards)
