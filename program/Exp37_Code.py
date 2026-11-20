import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

study_hours = np.array([1.5, 2.0, 3.0, 4.0, 4.5, 5.0, 6.0, 7.5, 8.0, 9.0])
exam_scores = np.array([45, 52, 60, 65, 72, 75, 82, 88, 92, 98])

corr, p_value = pearsonr(study_hours, exam_scores)

print("Study Time vs Exam Scores Analysis:")
print(f"Pearson Correlation Coefficient (r): {corr:.4f}")
print(f"P-value: {p_value:.4e}")
print("Relationship: Strong positive correlation observed.")

plt.figure(figsize=(7, 4))
plt.scatter(study_hours, exam_scores, color='blue', label='Student Data')
m, c = np.polyfit(study_hours, exam_scores, 1)
plt.plot(study_hours, m*study_hours + c, color='red', linestyle='--', label=f'Trend Line (r={corr:.2f})')
plt.title("Study Time vs Exam Score")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.legend()
plt.savefig("exp37_plot.png")
print("Scatter plot with trendline saved to exp37_plot.png.")
