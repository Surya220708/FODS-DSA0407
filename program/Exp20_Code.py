import numpy as np
from scipy import stats

np.random.seed(24)
# Conversion rates recorded across 30 observation days
design_A = np.random.normal(loc=0.12, scale=0.015, size=30)
design_B = np.random.normal(loc=0.15, scale=0.018, size=30)

t_stat, p_value = stats.ttest_ind(design_A, design_B)

print("E-commerce A/B Testing Results:")
print(f"Design A Mean Conversion Rate: {np.mean(design_A)*100:.2f}%")
print(f"Design B Mean Conversion Rate: {np.mean(design_B)*100:.2f}%")
print(f"T-statistic: {t_stat:.4f}, P-value: {p_value:.4e}")

alpha = 0.05
if p_value < alpha:
    print("Conclusion: Statistically significant difference exists between Design A and Design B (Reject H0).")
else:
    print("Conclusion: No statistically significant difference observed (Fail to reject H0).")
