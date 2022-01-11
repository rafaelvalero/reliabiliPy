# -*- coding: utf-8 -*-



name_notebook = 'revelle_ch7_example' # this is to save

import pandas as pd
import numpy as np

import sys
sys.path.append("../")


from reliabilipy import reliability_analysis

# Dataset as exmample in Table 7.5  https://personality-project.org/r/book/Chapter7.pdf

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

# McDonald's $ω_t$, which is similar to Guttman's $λ_6$, guttman but uses the estimates of uniqueness ($u^2$) from factor analysis to find $e_j^2$. This is based on a decomposition of the variance of a test score, $V_x$ into four parts: that due to a general factor, $\vec{g}$, that due to a set of group factors, $\vec{f}$, (factors common to some but not all of the items), specific factors, $\vec{s}$ unique to each item, and $\vec{e}$, random error. (Because specific variance can not be distinguished from random error unless the test is given at least twice, some combine these both into error).
#
# Letting $x = cg + Af + Ds + e$ then the communality of item_j, based upon general as well as group factors, $h_j^2 = c_j^2 + sum(f_ij^2)$ and the unique variance for the item $u_j^2 = σ_j^2 (1-h_j^2)$ may be used to estimate the test reliability. That is, if $h_j^2$ is the communality of item_j, based upon general as well as group factors, then for standardized items, $e_j^2 = 1 - h_j^2$ and
#
# $$ω_t =  \frac{1 cc' 1 + 1 AA' 1'}{V_x}$$
#
# Because $h_j^2 ≥q r_{smc}^2, ω_t ≥q λ_6$.
#
# It is important to distinguish here between the two ω coefficients of McDonald, 1978 and Equation 6.20a of McDonald, 1999, ω_t and ω_h. While the former is based upon the sum of squared loadings on all the factors, the latter is based upon the sum of the squared loadings on the general factor.
#
# $$ω_h =  \frac{1 cc' 1'}{Vx}$$
#
# Another estimate reported is the omega for an infinite length test with a structure similar to the observed test (omega H asymptotic). This is found by
#
# $$ω_{limit} = \frac{1 cc' 1'}{1 cc' 1' + 1 AA' 1'}$$
#
# .
#
# Following suggestions by Steve Reise, the Explained Common Variance (ECV) is also reported. This is the ratio of the general factor eigen value to the sum of all of the eigen values. As such, it is a better indicator of unidimensionality than of the amount of test variance accounted for by a general factor.
#
# The input to omega may be a correlation matrix or a raw data matrix, or a factor pattern matrix with the factor intercorrelations (Phi) matrix.

reliability_report = reliability_analysis(correlations_matrix=V)
reliability_report.fit()

print(reliability_report.omega_total)
print(reliability_report.omega_hierarchical)
print(reliability_report.omega_hierarchical_asymptotic)


# matrix $\mathbf{F}_{1}$ (i.e., rotated loadings), a first-order factorcorrelation matrix termed $\mathbf{R}_{1}$, and unique variances $\mathbf{U}_{1}^{2}$ of variables:
# $$
# \mathbf{R}_{v}=\mathbf{F}_{1} \mathbf{R}_{1} \mathbf{F}_{1}^{\prime}+\mathbf{U}_{1}^{2} .
# $$
# Matrix $\mathbf{F}_{1}$ is of the order $v \times f_{1}$, where $f_{1}$ is the number of first-order factors. $\mathbf{R}_{1}$ is of the order $f_{1} \times f_{1} . \mathbf{U}_{1}^{2}$ is a matrix of the order $v \times v$ and consists of measurement error and specific components of variables.
#
# Second-order factors can be extracted from the factor correlation matrix $\mathbf{R}_{1}$, yielding a matrix of second-order factor loadings $\mathbf{F}_{2}$, a second-order factor correlation matrix $\mathbf{R}_{2}$, and the unique variance of this level, $\mathbf{U}_{2}^{2}$ :
# $$
# \mathbf{R}_{1}=\mathbf{F}_{2} \mathbf{R}_{2} \mathbf{F}_{2}^{\prime}+\mathbf{U}_{2}^{2} .
# $$
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
# where $\mathbf{I}$ is an identity matrix and diag indicates that only



import os
order = f'jupytext --to py {name_notebook}.ipynb'
print(order)
os.system(order)

# +
import subprocess

subprocess.call(order, shell=True)
# -

# !jupytext --to py revelle_ch7_example.ipynb


