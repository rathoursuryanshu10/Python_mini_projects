import numpy as np
from scipy.stats import chi2_contingency
data=np.array([[30,10],[20,25]])
chi2_stat,p_val,dof,exepected=chi2_contingency(data)
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-Value: {p_val}")
print(f"Degree of Freedom : {dof}")
print("Expected Frequency : ")
print(exepected)
