import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_players.csv")

print("1. Top 5 Goal Scorers:")
print(df.nlargest(5, 'goals')[['name', 'goals', 'position']])

print("\n2. Top 5 Highest Weekly Salaries:")
print(df.nlargest(5, 'weekly_salary')[['name', 'weekly_salary', 'position']])

avg_age = df['age'].mean()
print(f"\n3. Average Player Age: {avg_age:.1f} years")
above_avg = df[df['age'] > avg_age]['name'].tolist()
print(f"Players Above Average Age: {', '.join(above_avg)}")

# Bar chart of player positions
pos_counts = df['position'].value_counts()
plt.figure(figsize=(7, 4))
pos_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.tight_layout()
plt.savefig("exp40_plot.png")
print("\nPosition distribution bar chart saved to exp40_plot.png.")
