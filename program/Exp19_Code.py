import numpy as np
from scipy import stats

np.random.seed(42)
# Sample of 50 patients: drug reduction vs placebo reduction
drug_group = np.random.normal(loc=14.5, scale=4.0, size=50)
placebo_group = np.random.normal(loc=3.2, scale=3.5, size=50)

def get_ci(data, confidence=0.95):
    mean = np.mean(data)
    sem = stats.sem(data)
    ci = stats.t.interval(confidence, len(data) - 1, loc=mean, scale=sem)
    return mean, ci

drug_mean, drug_ci = get_ci(drug_group)
plac_mean, plac_ci = get_ci(placebo_group)

print("95% Confidence Intervals for Blood Pressure Reduction:")
print(f"Drug Group    : Mean = {drug_mean:.2f} mmHg | 95% CI = [{drug_ci[0]:.2f}, {drug_ci[1]:.2f}]")
print(f"Placebo Group : Mean = {plac_mean:.2f} mmHg | 95% CI = [{plac_ci[0]:.2f}, {plac_ci[1]:.2f}]")
