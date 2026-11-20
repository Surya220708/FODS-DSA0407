import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("customer_reviews.csv")
ratings = df['rating']

n = len(ratings)
mean_rating = ratings.mean()
std_rating = ratings.std(ddof=1)
sem = stats.sem(ratings)
ci = stats.t.interval(0.95, n - 1, loc=mean_rating, scale=sem)

print("Customer Reviews Rating Confidence Interval Analysis:")
print(f"Total Reviews (n): {n}")
print(f"Sample Mean Rating: {mean_rating:.2f} / 5.0")
print(f"Sample Standard Deviation: {std_rating:.2f}")
print(f"Standard Error of Mean: {sem:.3f}")
print(f"95% Confidence Interval for True Mean Rating: [{ci[0]:.2f}, {ci[1]:.2f}]")
