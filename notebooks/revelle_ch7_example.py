# -*- coding: utf-8 -*-
#
#
# # Aim
#
# To provide a clear understanding of some of the key measures or reliability and their implementation in `python`.
#
# # How
#
# To do that I will follow references as close as possible while providing the python code of the implementation of the ideas and examples.
#
# Revelle has greatly created and write many papers in the matter and the library `psych`in `R` with the corresponding implementations. We would follow Revelle 2021 and 2017, in particlar Revelle 2021 very closely.
#
# We would expand a bit when calculating the omegas and in particular when using the `Schmid-Leiman` solution, following Wolff and Presing 2005, as it constains a clear explanations of the theory and the estimation, as in this paper authors describe the implementation in `SPSS` and `SAS`, which something similar we are trying to do here in `python`.
#
#
# ## References
# * Revelle, Willian. Manuscrip. 2021. An introduction to psychometric theory with applications in R. https://personality-project.org/r/book/Chapter7.pdf
# * Revelle, William R. "psych: Procedures for personality and psychological research." (2017).
# * Wolff, Hans-Georg, and Katja Preising. "Exploring item and higher order factor structure with the Schmid-Leiman solution: Syntax codes for SPSS and SAS." Behavior Research Methods 37.1 (2005): 48-58.
#
# Examples in R.
#
# This work: 
# * Rafael Valero Fernández. (2022). reliabiliPy: measures of survey domain reliability in Python with explanations and examples. Cronbach´s Alpha and Omegas. (v0.0.0). Zenodo.[![DOI](https://zenodo.org/badge/445846537.svg)](https://zenodo.org/badge/latestdoi/445846537) 

name_notebook = 'revelle_ch7_example' # this is to save

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

Vx=V.sum().sum()
print(Vx)

# $$
# \lambda_{1}=1-\frac{\operatorname{tr}\left(\mathbf{V}_{\mathbf{x}}\right)}{V_{x}}=\frac{V_{x}-\operatorname{tr}\left(\mathbf{V}_{x}\right)}{V_{x}} .
# $$
# In the example:
# $$
# \lambda_{1}=1-\frac{12}{53.2}=\frac{41.2}{53.2}=.774
# $$

lambda1 = 1 - np.diag(V).sum() / Vx
print(lambda1)

# Let $C_{2}=\mathbf{1}(\mathbf{V}-\operatorname{diag}(\mathbf{V}))^{2} \mathbf{1}^{\prime}$, then
# $$
# \lambda_{2}=\lambda_{1}+\frac{\sqrt{\frac{n}{n-1} C_{2}}}{V_{x}}=\frac{V_{x}-\operatorname{tr}\left(\mathbf{V}_{x}\right)+\sqrt{\frac{n}{n-1} C_{2}}}{V_{x}} 
# $$

n=V.shape[0]
C2=((V - np.eye(n)*np.diag(V))**2).sum().sum()
print(C2)

lambda2=lambda1+(n/(n-1)*C2)**0.5/Vx
print(lambda2)

# $$\lambda_{3}=\lambda_{1}+\frac{\frac{V_{X}-\operatorname{tr}\left(\mathbf{V}_{X}\right)}{n(n-1)}}{V_{X}}=\frac{n \lambda_{1}}{n-1}=\frac{n}{n-1}\left(1-\frac{\operatorname{tr}(\mathbf{V})_{x}}{V_{x}}\right)=\frac{n}{n-1} \frac{V_{x}-\operatorname{tr}\left(\mathbf{V}_{x}\right)}{V_{x}}=\alpha$$

alpha = n/(n-1)*(Vx-np.diag(V).sum())/Vx
print(alpha)

reliability_report = reliability_analysis(correlations_matrix=V)
reliability_report.fit()
print(reliability_report.lambda1)
print(reliability_report.lambda2)
print(reliability_report.alpha_cronbach)

# # Omegas reliability
#
# Omegas are based on a decomposition of the variance of a test score, $V_x$ into four parts: that due to a general factor, $\vec{g}$, that due to a set of group factors, $\vec{f}$, (factors common to some but not all of the items), specific factors, $\vec{s}$ unique to each item, and $\vec{e}$, random error. (Because specific variance can not be distinguished from random error unless the test is given at least twice, some combine these both into error).
#
# $$
# \begin{equation} \label{eq:1}
# x = cg + Af + Ds + e
# \end{equation}
# $$
#
# then the communality of item $j$, based upon general as well as group factors, $h_j^2 = c_j^2 + \sum(f_{ij}^2)$ and the unique variance for the item $u_j^2 = σ_j^2 (1-h_j^2)$ may be used to estimate the test reliability. That is, if $h_j^2$ is the communality of item $j$, based upon general as well as group factors, then for standardized items, $e_j^2 = 1 - h_j^2$ and
#
# $$ω_t =  \frac{1 cc' 1 + 1 AA' 1'}{V_x}$$
#
#
# $ω_t$ is based upon the sum of squared loadings on all the factors.
# $ω_h$ is based upon the sum of the squared loadings on the general factor.
#
# $$ω_h =  \frac{1 cc' 1'}{Vx}$$
#
# Another estimate reported is the omega for an infinite length test with a structure similar to the observed test (omega hierarchical asymptotic). This is found by
#
# $$ω_{limit} = \frac{1 cc' 1'}{1 cc' 1' + 1 AA' 1'}$$
#
#
# The input to omega may be a correlation matrix or a raw data matrix, or a factor pattern matrix with the factor intercorrelations (Phi) matrix.

# ## Results in R using Psych
# There is an R notebook with the full example, in the same folder that this notebook, with this result:
# ```bash
# Omega 
# Call: omega(m = correlation_matrix)
# Alpha:                 0.84 
# G.6:                   0.88 
# Omega Hierarchical:    0.54 
# Omega H asymptotic:    0.6 
# Omega Total            0.9 
# ````
#

# ## Results using 'reliabiliPy'

reliability_report = reliability_analysis(correlations_matrix=V)
reliability_report.fit()

print(reliability_report.omega_total)
print(reliability_report.omega_hierarchical)
print(reliability_report.omega_hierarchical_asymptotic)


# ## Further R output
# ```bash
#     g        F1   F2   F3     h2      u2      p2
# v0	0.45	0.55			0.5	0.5	0.40
# v1	0.45	0.55			0.5	0.5	0.40
# v2	0.45	0.55			0.5	0.5	0.40
# v3	0.45	0.55			0.5	0.5	0.40
# v4	0.45	0.55			0.5	0.5	0.40
# v5	0.45	0.55			0.5	0.5	0.40
# v6	0.45		 0.63	   0.6	0.4	0.33
# v7	0.45		 0.63	   0.6	0.4	0.33
# v8	0.45		 0.63	   0.6	0.4	0.33
# v9	0.45		 0.63	   0.6	0.4	0.33
# ```
#
# With eigenvalues of:
# ```bash
#   g F1* F2* F3* 
# 2.4 1.8 1.6 1.0 
# ```

reliability_report.report_loadings['g'][0]

reliability_report.report_eigenvalues

# # Estimation of Omegas reliabilities
#
# This section is in case you want to go deeper. This will allow you to understand the calculation and to be able to modify the package.
#
# But how can we estimate that?. Using `Schmid-Leiman` solution. For an explanation on that   Wolff and Preising (2005). There the authors try to do the same that in this work but for SPSS and SAS. 
#
# "matrix $\mathbf{F}_{1}$ (i.e., rotated loadings), a first-order factor correlation matrix termed $\mathbf{R}_{1}$, and unique variances $\mathbf{U}_{1}^{2}$ of variables:
# $$
# \mathbf{R}_{v}=\mathbf{F}_{1} \mathbf{R}_{1} \mathbf{F}_{1}^{\prime}+\mathbf{U}_{1}^{2} 
# $$
#
#
#
# Matrix $\mathbf{F}_{1}$ is of the order $v \times f_{1}$, where $f_{1}$ is the number of first-order factors. $\mathbf{R}_{1}$ is of the order $f_{1} \times f_{1} . \mathbf{U}_{1}^{2}$ is a matrix of the order $v \times v$ and consists of measurement error and specific components of variables.
#
# Second-order factors can be extracted from the factor correlation matrix $\mathbf{R}_{1}$, yielding a matrix of second-order factor loadings $\mathbf{F}_{2}$, a second-order factor correlation matrix $\mathbf{R}_{2}$, and the unique variance of this level, $\mathbf{U}_{2}^{2}$ :
#
#
#
# $$
# \mathbf{R}_{1}=\mathbf{F}_{2} \mathbf{R}_{2} \mathbf{F}_{2}^{\prime}+\mathbf{U}_{2}^{2}
# $$
#
#
# $\mathbf{F}_{2}$ is of the order $f_{1} \times f_{2}$, where $f_{2}$ is the number of second-order factors. $\mathbf{R}_{2}$ is of the order $f_{2} \times f_{2} . \mathbf{U}_{2}^{2}$ is a matrix of the order $f_{1} \times f_{1}$.
#
# These two analyses comprise a minimal higher order FA consisting of two levels. $\mathbf{F}_{1}$ from Equation 1 provides first-order factor loadings (e.g., paths from $\mathrm{F}_{1}$ to variables in Figure 1A), and $\mathbf{F}_{2}$ yields second-order factor loadings (e.g., the path from Factor 1 to $\mathrm{F}_{1}$ in Figure $1 \mathrm{~A}$ ). If second-order factors are uncorrelated, matrix $\mathbf{R}_{2}$ is an identity matrix and can be ignored. If second-order factors are correlated, analyses may continue to extract third-order factors.
#
# To obtain the SLS, two further calculations are necessary. In a first step, direct effects of higher order factors on variables are determined by multiplying all factor-loading matrices from first to highest order. In the present case, the direct loadings of second-order factors on variables, termed $\mathbf{F}_{2}^{S L S}$, are obtained by multiplying $\mathbf{F}_{1} \times \mathbf{F}_{2}$
# $$
# \mathbf{F}_{2}^{\mathrm{SLS}}=\mathbf{F}_{1} * \mathbf{F}_{2},
# $$
# where $\mathbf{F}_{2}^{\text {SLS }}$ is of the order $v \times f_{2}$. To obtain residualized first-order factor loadings $\mathbf{F}_{1}^{\mathrm{SLS}}$, factor loadings $\mathbf{F}_{1}$ are multiplied by the uniqueness $\mathbf{U}_{2}$ of higher order factors:
# $$
# \mathbf{F}_{1}^{\mathrm{SLS}}=\mathbf{F}_{1} * \mathbf{U}_{2},
# $$
# where $\mathbf{F}_{1}^{\mathrm{SLS}}$ is of the order $v \times f_{1}$. The uniqueness $\mathbf{U}_{2}$ is equivalent to the square root of the variances of $\mathbf{R}_{1}$ not explained by higher order factors. It is obtained by subtracting the explained variance of a factor from 1:
# $$
# \mathbf{U}_{2}=\left[\mathbf{I}-\operatorname{diag}\left(\mathbf{F}_{2} \mathbf{R}_{2} \mathbf{F}_{2}^{\prime}\right)\right]^{0.5},
# $$
# where $\mathbf{I}$ is an identity matrix and diag indicates that only"

# # Tranlations in our case and to Python
# $$
# \mathbf{F}_{2}^{\mathrm{SLS}}=\mathbf{F}_{1} * \mathbf{F}_{2},
# $$
# implementation in `python`:

general_component = np.dot(reliability_report.fa_f.loadings_,
                           reliability_report.fa_g.loadings_)
general_component=np.abs(general_component)
general_component

# Eigenvalue g

np.dot(general_component.T,general_component)

# # $u^2$ in our example:

reliability_report.fa_f.get_uniquenesses()

# # $h^2$ in our example:

reliability_report.fa_f.get_communalities()

# To update the group factors
#
# $$
# \mathbf{F}_{1}^{\mathrm{SLS}}=\mathbf{F}_{1} * \mathbf{U}_{2},
# $$

f_loadings_final = np.zeros(reliability_report.fa_f.loadings_.shape)
f_loadings_final


reliability_report.fa_g.loadings_

reliability_report.fa_f.get_uniquenesses()

# +
for i in range(0,reliability_report.fa_g.get_uniquenesses().__len__()):
    f_loadings_final[:,i] = reliability_report.fa_f.loadings_[:,i]*reliability_report.fa_g.get_uniquenesses()[i]**0.5

f_loadings_final = np.abs(f_loadings_final)   
# -

# The eigenvectors in our example:

np.abs(f_loadings_final).round(3)

# The eigenvalues:

np.dot(f_loadings_final.T,f_loadings_final).sum(axis=1)

"""save code """

import os
order = f'jupytext --to py {name_notebook}.ipynb'
print(order)
os.system(order)
