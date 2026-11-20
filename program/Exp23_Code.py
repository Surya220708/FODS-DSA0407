import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(10)
placebo = np.random.normal(loc=50, scale=8, size=40)
treatment = np.random.normal(loc=62, scale=7, size=40)

t_stat, p_val = stats.ttest_ind(treatment, placebo)

print("Clinical Trial Hypothesis Testing:")
print(f"Placebo Mean: {np.mean(placebo):.2f}, Treatment Mean: {np.mean(treatment):.2f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.5e}")
if p_val < 0.05:
    print("Verdict: The new treatment shows a statistically significant improvement over placebo.")

plt.figure(figsize=(7, 4))
plt.boxplot([placebo, treatment], labels=['Placebo Group', 'Treatment Group'])
plt.title(f"Clinical Trial Comparison (p-value = {p_val:.2e})")
plt.ylabel("Outcome Measurement")
plt.savefig("exp23_plot.png")
print("Plot saved to exp23_plot.png.")
