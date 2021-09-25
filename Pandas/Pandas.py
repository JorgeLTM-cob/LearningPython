import pandas as pd
import numpy as np

data = pd.DataFrame({'Yes': [50,21], 'No':[131,2]})
print(data)

data1 = pd.DataFrame({'Bob' : ['I liked it.', 'It was awful.'],
                      'Sue' : ['Pretty good.', 'Bland.']},
                     index = ['Product A', 'Product B'])

print(data1)

data2 = pd.Series([1, 2, 3, 4, 5])
print(data2)

data3 = pd.Series([30, 35, 40], index = ['2015 Sales', '2016 Sales', '2017 Sales'], name = 'ProductA')
print(data3)
