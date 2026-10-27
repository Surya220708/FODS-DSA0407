import numpy as np

fuel_efficiency = np.array([25, 30, 35, 40])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Compare the first and second car models
model1 = fuel_efficiency[0]
model2 = fuel_efficiency[1]

# Calculate percentage improvement
improvement = ((model2 - model1) / model1) * 100

print("Average Fuel Efficiency:", average_efficiency, "miles per gallon")
print("Percentage Improvement:", improvement, "%")
