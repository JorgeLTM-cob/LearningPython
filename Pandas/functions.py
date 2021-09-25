import pandas as pd
import numpy as np

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews = pd.read_csv("wines.csv", index_col = 0)
#print(reviews.points.describe())
#print(reviews.taster_name.describe())
#print(reviews.points.mean())
#print(reviews.taster_name.unique())
#print(reviews.taster_name.value_counts())
#review_points_mean = reviews.points.mean()
#print(reviews.points.map(lambda p: p - review_points_mean))
#print(reviews.apply(remean_points, axis='columns'))
#print(reviews.points - review_points_mean)
print(reviews.country + " - " + reviews.region_1)
