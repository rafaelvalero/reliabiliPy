name_notebook = 'revelle_ch7_example_short' # this is to save

# %load_ext autoreload
# %autoreload 2
import pandas as pd
import numpy as np
import sys
sys.path.append("../")
from reliabilipy import reliability_analysis

# Dataset as examample in Table 7.5  https://personality-project.org/r/book/Chapter7.pdf

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

# Lets try to stimate different reliability measures

reliability_report = reliability_analysis(correlations_matrix=V)
reliability_report.fit()
print(reliability_report.lambda1)
print(reliability_report.lambda2)
print(reliability_report.alpha_cronbach)

print(reliability_report.omega_total)
print(reliability_report.omega_hierarchical)
print(reliability_report.omega_hierarchical_asymptotic)

reliability_report.report_eigenvalues

reliability_report.report_loadings

# The eigenvalues:

np.dot(f_loadings_final.T,f_loadings_final).sum(axis=1)

"""save code """

import os
order = f'jupytext --to py {name_notebook}.ipynb'
print(order)
os.system(order)
