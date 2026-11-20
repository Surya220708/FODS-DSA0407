import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temp = [24, 26, 29, 32, 35, 33, 31, 30, 30, 28, 26, 25]
rainfall = [20, 15, 10, 25, 60, 120, 180, 160, 140, 210, 190, 80]

print("Monthly Climate Summary:")
print(f"Highest Temperature: {max(temp)}°C in {months[temp.index(max(temp))]}")
print(f"Lowest Temperature: {min(temp)}°C in {months[temp.index(min(temp))]}")
print(f"Total Annual Rainfall: {sum(rainfall)} mm")
print(f"Peak Rainfall Month: {months[rainfall.index(max(rainfall))]} ({max(rainfall)} mm)")

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(months, temp, marker='o', color='red')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")

plt.subplot(1, 2, 2)
plt.scatter(months, rainfall, color='blue')
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("exp12_plot.png")
print("Temperature & Rainfall plots generated successfully.")
