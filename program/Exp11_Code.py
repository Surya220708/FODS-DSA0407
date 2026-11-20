import matplotlib.pyplot as plt

# Monthly Product Sales Visualization
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [4500, 5200, 4800, 6100, 7000, 6800]
days = [1, 5, 10, 15, 20, 25, 30]
daily_sales = [120, 150, 180, 220, 260, 300, 340]

print("Monthly Product Sales Data:")
for m, s in zip(months, sales):
    print(f"{m}: ${s}")

total_sales = sum(sales)
avg_sales = total_sales / len(sales)
print(f"Total Sales: ${total_sales}")
print(f"Average Monthly Sales: ${avg_sales:.2f}")

# Generating Visualization plots
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(days, daily_sales, marker='o', color='blue')
plt.title("Predicted Daily Sales (Line Plot)")
plt.xlabel("Day of Month")
plt.ylabel("Sales ($)")

plt.subplot(1, 2, 2)
plt.bar(months, sales, color='orange')
plt.title("Monthly Sales Data (Bar Plot)")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("exp11_plot.png")
print("Visualizations successfully generated and saved to exp11_plot.png.")
