import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("rare_elements.csv")
sample_size = 40
confidence_level = 0.95
precision_desired = 1.5

sample = df['concentration'].sample(n=sample_size, random_state=42)
mean_est = np.mean(sample)
sem = stats.sem(sample)
ci = stats.t.interval(confidence_level, sample_size - 1, loc=mean_est, scale=sem)
margin_of_error = ci[1] - mean_est

print("Rare Element Point Estimation & Confidence Interval:")
print(f"Sample Size (n): {sample_size}")
print(f"Point Estimate (Sample Mean): {mean_est:.3f} ppm")
print(f"{int(confidence_level*100)}% Confidence Interval: [{ci[0]:.3f}, {ci[1]:.3f}] ppm")
print(f"Margin of Error: ±{margin_of_error:.3f} ppm (Desired precision: ±{precision_desired} ppm)")
