# Computations
import pandas as pd
import numpy as np
from factor_analyzer import FactorAnalyzer
# import doctest

from typing import List, Tuple, Union, Mapping, Any


class reliability_analysis:
    """

    Usage:

    ```python
    ```

    >>> import pandas as pd
    >>> import numpy as np
    >>> from omegapy import reliability_analysis
    >>> correlations_matrix = pd.DataFrame(np.matrix([[1., 0.483, 0.34, 0.18, 0.277, 0.257, -0.074, 0.212, 0.226],\
                                      [0.483, 1., 0.624, 0.26, 0.433, 0.301, -0.028, 0.362, 0.236],\
                                      [0.34, 0.624, 1., 0.24, 0.376, 0.244, 0.233, 0.577, 0.352],\
                                      [0.18, 0.26, 0.24, 1., 0.534, 0.654, 0.165, 0.411, 0.306],\
                                      [0.277, 0.433, 0.376, 0.534, 1., 0.609, 0.041, 0.3, 0.239],\
                                      [0.257, 0.301, 0.244, 0.654, 0.609, 1., 0.133, 0.399, 0.32],\
                                      [-0.074, -0.028, 0.233, 0.165, 0.041, 0.133, 1., 0.346, 0.206],\
                                      [0.212, 0.362, 0.577, 0.411, 0.3, 0.399, 0.346, 1., 0.457],\
                                      [0.226, 0.236, 0.352, 0.306, 0.239, 0.32, 0.206, 0.457, 1.]]))
    >>> reliability_report = reliability_analysis(correlations_matrix=correlations_matrix)
    >>> reliability_report.fit()
    >>> reliability_report.omega_hierarchical
    0.5451484335574861
    >>> reliability_report.omega_total
    0.8579745972600469
    >>> reliability_report.omega_hierarchical_asymptotic
    0.6353899466236236
    >>> reliability_report.alpha_cronbach
    0.803183205136355
    """

    def __init__(self,
                 correlations_matrix = None,
                 method_fa_f: str = 'minres',
                 rotation_fa_f: str = 'oblimin',
                 method_fa_g: str = 'minres',
                 is_corr_matrix: bool = True,
                 n_factors_f: int = 3):
        """
        Initialization of the class.
        Set up all key variables and options for the analysis

        :param self:
        :param correlations_matrix:
        :param method_fa_f:
        :param rotation_fa_f:
        :param method_fa_g:
        :param is_corr_matrix:
        :param n_factors_f:
        :return:
        """
        self.omega_hierarchical = None
        self.correlations_matrix = correlations_matrix
        self.method_fa_f = method_fa_f
        self.rotation_fa_f = rotation_fa_f
        self.method_fa_g = method_fa_g
        self.is_corr_matrix = is_corr_matrix
        self.n_factors_f = n_factors_f
        self.fa_f = None
        self.fa_g = None
        self.general_component = None
        self.omega_hierarchical = None
        self.omega_total = None
        self.omega_hierarchical_asymptotic = None
        self.alpha_cronbach = None


    def fit(self):
        self.fa_f = FactorAnalyzer(rotation=self.rotation_fa_f,
                                   method=self.method_fa_f,
                                   is_corr_matrix=self.is_corr_matrix)
        self.fa_f.fit(self.correlations_matrix)
        self.fa_g = FactorAnalyzer(rotation=None,
                                   is_corr_matrix=True,
                                   method=self.method_fa_g,
                                   n_factors=1)
        self.fa_g.fit(self.fa_f.phi_)
        # Omega Report
        self.general_component = np.dot(self.fa_f.loadings_, self.fa_g.loadings_)
        Vt = self.correlations_matrix.sum().sum()
        Vitem = sum(np.diag(self.correlations_matrix))
        gsq = self.general_component.sum() ** 2
        uniq = self.fa_f.get_uniquenesses().sum()
        # From now we assume that data is in wide format
        n, k = self.correlations_matrix.shape
        nvar = k
        self.omega_hierarchical = gsq / Vt
        self.omega_total = (Vt - uniq) / Vt
        self.omega_hierarchical_asymptotic = gsq / (Vt - uniq)
        # Alpha calculations
        self.alpha_cronbach = ((Vt - Vitem) / Vt) * (nvar / (nvar - 1))


if __name__ == "__main__":

    df_features = pd.DataFrame(np.matrix([[1., 0.483, 0.34, 0.18, 0.277, 0.257, -0.074, 0.212, 0.226],
                                          [0.483, 1., 0.624, 0.26, 0.433, 0.301, -0.028, 0.362, 0.236],
                                          [0.34, 0.624, 1., 0.24, 0.376, 0.244, 0.233, 0.577, 0.352],
                                          [0.18, 0.26, 0.24, 1., 0.534, 0.654, 0.165, 0.411, 0.306],
                                          [0.277, 0.433, 0.376, 0.534, 1., 0.609, 0.041, 0.3, 0.239],
                                          [0.257, 0.301, 0.244, 0.654, 0.609, 1., 0.133, 0.399, 0.32],
                                          [-0.074, -0.028, 0.233, 0.165, 0.041, 0.133, 1., 0.346, 0.206],
                                          [0.212, 0.362, 0.577, 0.411, 0.3, 0.399, 0.346, 1., 0.457],
                                          [0.226, 0.236, 0.352, 0.306, 0.239, 0.32, 0.206, 0.457, 1.]]))

    df_features

    # +
    rotation = 'oblimin'
    method = 'minres'

    fa = FactorAnalyzer(rotation=rotation,
                        method=method,
                        is_corr_matrix=True)
    fa.fit(df_features)
    # -

    fa2 = FactorAnalyzer(rotation=None,
                         is_corr_matrix=True,
                         method='minres',
                         n_factors=1)
    fa2.fit(fa.phi_)

    general_component = np.dot(fa.loadings_, fa2.loadings_)
    general_component

    Vt = df_features.sum().sum()
    Vt

    Vitem = sum(np.diag(df_features))
    Vitem

    gsq = general_component.sum() ** 2
    # gsq = fa2.loadings_.sum()**2
    gsq

    uniq = fa.get_uniquenesses().sum()
    uniq

    # From now we assume that data is in wide format
    n, k = df_features.shape
    nvar = k
    nvar

    omega_hierarchical = gsq / Vt
    omega_hierarchical

    omega_total = (Vt - uniq) / Vt
    omega_total

    # omega_hierarchical_asymptotic
    omega_hierarchical_asymptotic = gsq / (Vt - uniq)
    omega_hierarchical_asymptotic

    reliability_report = reliability_analysis(correlations_matrix=df_features)
    reliability_report.fit()