import pandas as pd
import numpy as np
from reliabilipy import reliability_analysis

"""
Dataset as exmample in Table 7.5  https://personality-project.org/r/book/Chapter7.pdf
"""

V = pd.DataFrame(np.matrix([[1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
[0.5, 1.0, 0.5, 0.5, 0.5, 0.5, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
[0.5, 0.5, 1.0, 0.5, 0.5, 0.5, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
[0.5, 0.5, 0.5, 1.0, 0.5, 0.5, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
[0.5, 0.5, 0.5, 0.5, 1.0, 0.5, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
[0.5, 0.5, 0.5, 0.5, 0.5, 1.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 1.0, 0.6, 0.6, 0.6, 0.2, 0.2],
[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.6, 1.0, 0.6, 0.6, 0.2, 0.2],
[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.6, 0.6, 1.0, 0.6, 0.2, 0.2],
[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.6, 0.6, 0.6, 1.0, 0.2, 0.2],
[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 1.0, 0.7],
[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.7, 1.0]]))

Vx=V.sum().sum()
print(Vx)

lambda1 = 1 - np.diag(V).sum() / Vx
print(lambda1)

n=V.shape[0]
C2=((V - np.eye(n)*np.diag(V))**2).sum().sum()
print(C2)

lambda2=lambda1+(n/(n-1)*C2)**0.5/Vx
print(lambda2)

alpha = n/(n-1)*(Vx-np.diag(V).sum())/Vx
print(alpha)

reliability_report = reliability_analysis(correlations_matrix=V)
reliability_report.fit()

print(reliability_report.omega_total)
print(reliability_report.omega_hierarchical)
print(reliability_report.omega_hierarchical_asymptotic)

