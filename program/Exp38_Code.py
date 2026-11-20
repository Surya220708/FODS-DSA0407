import numpy as np
import pandas as pd

np.random.seed(42)
days = 365
cities = {
    'Chennai': np.random.normal(loc=31.0, scale=3.2, size=days),
    'Delhi': np.random.normal(loc=25.0, scale=8.5, size=days),
    'Bangalore': np.random.normal(loc=23.5, scale=2.4, size=days),
    'Mumbai': np.random.normal(loc=28.0, scale=2.8, size=days)
}

print("Weather Temperature Variability Analysis:")
stats_list = []
for city, temps in cities.items():
    mean_t = np.mean(temps)
    std_t = np.std(temps)
    rng_t = np.ptp(temps)
    stats_list.append({'City': city, 'Mean': mean_t, 'Std_Dev': std_t, 'Range': rng_t})
    print(f"{city:<10}: Mean = {mean_t:.2f}°C, Std Dev = {std_t:.2f}°C, Range = {rng_t:.2f}°C")

df_stats = pd.DataFrame(stats_list)
max_range_city = df_stats.loc[df_stats['Range'].idxmax()]['City']
consistent_city = df_stats.loc[df_stats['Std_Dev'].idxmin()]['City']

print(f"\n1. City with Highest Temperature Range: {max_range_city}")
print(f"2. City with Most Consistent Temperature: {consistent_city}")
