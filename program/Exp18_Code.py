import pandas as pd
import matplotlib.pyplot as plt

data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    'fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

df = pd.DataFrame(data)

print("Hospital Data Statistical Summary:")
print(f"Age Mean: {df['age'].mean():.2f}, Median: {df['age'].median():.2f}, Std Dev: {df['age'].std():.2f}")
print(f"%Fat Mean: {df['fat'].mean():.2f}, Median: {df['fat'].median():.2f}, Std Dev: {df['fat'].std():.2f}")

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].boxplot([df['age'], df['fat']], labels=['Age', '%Fat'])
axs[0].set_title("Boxplots for Age and %Fat")

axs[1].scatter(df['age'], df['fat'], color='purple')
axs[1].set_title("Scatter Plot: Age vs %Fat")
axs[1].set_xlabel("Age")
axs[1].set_ylabel("%Fat")
plt.tight_layout()
plt.savefig("exp18_plot.png")
print("Boxplot and scatter plot saved to exp18_plot.png.")
