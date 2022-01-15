# Computations
import pandas as pd
import numpy as np
from factor_analyzer import FactorAnalyzer
from factor_analyzer.utils import impute_values, corr
# import doctest
from typing import List, Tuple, Union, Mapping, Any

POSSIBLE_IMPUTATIONS = ['mean', 'median', 'drop']
# This options are to alling with factor_analyzer package
POSSIBLE_METHODS = ['ml', 'mle', 'uls', 'minres', 'principal']
ORTHOGONAL_ROTATIONS = ['varimax', 'oblimax', 'quartimax', 'equamax', 'geomin_ort']
OBLIQUE_ROTATIONS = ['promax', 'oblimin', 'quartimin', 'geomin_obl']
POSSIBLE_ROTATIONS = ORTHOGONAL_ROTATIONS + OBLIQUE_ROTATIONS


class reliability_analysis:
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

    Examples
    -------
    With correlations matrix
    >>> import pandas as pd
    >>> import numpy as np
    >>> from reliabilipy import reliability_analysis
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
    >>> np.testing.assert_almost_equal(reliability_report.lambda1, 0.7139, decimal=3)
    >>> np.testing.assert_almost_equal(reliability_report.lambda2, 0.8149701194973398, decimal=3)

    With dataset and imputations:

    >>> import pandas as pd
    >>> import numpy as np
    >>> from reliabilipy import reliability_analysis
    >>> raw_dataset = pd.DataFrame([{'C1': 2.0, 'C2': 3.0, 'C3': 3.0, 'C4': 4.0, 'C5': 4.0},\
        {'C1': 5.0, 'C2': 4.0, 'C3': 4.0, 'C4': 3.0, 'C5': 4.0},\
        {'C1': 4.0, 'C2': 5.0, 'C3': 4.0, 'C4': 2.0, 'C5': 5.0},\
        {'C1': 4.0, 'C2': 4.0, 'C3': 3.0, 'C4': 5.0, 'C5': 5.0},\
        {'C1': 4.0, 'C2': 4.0, 'C3': 5.0, 'C4': 3.0, 'C5': 2.0},\
        {'C1': 4.0, 'C2': np.nan, 'C3': 3.0, 'C4': 5.0, 'C5': 5.0},\
        {'C1': np.nan, 'C2': 4.0, 'C3': 5.0, 'C4': 3.0, 'C5': 2.0}])
    >>> ra = reliability_analysis(raw_dataset=raw_dataset,\
                              is_corr_matrix=False,\
                              impute='median')
    >>> ra.fit()
    >>> np.testing.assert_almost_equal(reliability_report.alpha_cronbach, 0.78917, decimal=3)
    >>> np.testing.assert_almost_equal(reliability_report.omega_total, 0.9378722, decimal=3)

    """

    def __init__(self,
                 correlations_matrix=None,
                 raw_dataset=None,
                 method_fa_f: str = 'minres',
                 rotation_fa_f: str = 'oblimin',
                 method_fa_g: str = 'minres',
                 is_corr_matrix: bool = True,
                 impute: str = 'drop',
                 n_factors_f: int = 3):

        self.raw_dataset = raw_dataset
        self.correlations_matrix = correlations_matrix
        self.method_fa_f = method_fa_f.lower()
        self.rotation_fa_f = rotation_fa_f.lower()
        self.method_fa_g = method_fa_g.lower()
        self.is_corr_matrix = is_corr_matrix
        self.n_factors_f = n_factors_f
        self.impute = impute
        # Defaults to None
        self.fa_f = None
        self.fa_g = None
        self.general_component = None
        self.omega_hierarchical = None
        self.omega_total = None
        self.omega_hierarchical_asymptotic = None
        self.alpha_cronbach = None
        self.general_component_loading = None
        self.lambda2 = None
        self.lambda1 = None
        self.general_component_eigenvalue = None
        self.f_eigenvalues_final = None
        self.f_loadings_final = None
        self.omega_hierarchical = None
        self.raw_dataset_imputated = None

    def _argument_checker(self):
        """
        This is to check the arguments from the beginning.

        """
        if not isinstance(self.raw_dataset,type(None)) and self.is_corr_matrix==True:
            raise ValueError(f"You have introduced variable 'raw_dataset' and "
                             f"'is_corr_matrix' as True. If 'is_corr_matrix' then"
                             f"you should use 'correlations_matrix' instead of "
                             f"'raw_dataset'.")

        if isinstance(self.correlations_matrix,type(None)) and self.is_corr_matrix==True:
            raise ValueError(f"If 'is_corr_matrix' is True, please introduce it in "
                             f"'correlations_matrix' = YOUR DATA")

        self.impute = self.impute.lower() if isinstance(self.impute, str) else self.impute
        if self.impute not in POSSIBLE_IMPUTATIONS:
            raise ValueError(f"The imputation must be one of the following: {POSSIBLE_IMPUTATIONS}")

        self.rotation_fa_f = self.rotation_fa_f.lower() if isinstance(self.rotation_fa_f, str) else self.rotation_fa_f
        if self.rotation_fa_f not in POSSIBLE_ROTATIONS + [None]:
            raise ValueError(f"The rotation must be one of the following: {POSSIBLE_ROTATIONS + [None]}")

        for method_ in [self.method_fa_f, self.method_fa_g]:
            method_ = method_.lower() if isinstance(method_, str) else method_
            if method_ not in POSSIBLE_METHODS:
                raise ValueError(f"The method must be one of the following: {POSSIBLE_METHODS}")

    def fit(self):
        """
        Here the key calculations happens.
        See notebook with explanations.
        """
        # check the input arguments. To make sure everything is according to
        # FactorAnalyzer
        self._argument_checker()
        # convert to numpy

        # check to see if there are any null values, and if
        # so impute using the desired imputation approach
        if not isinstance(self.raw_dataset,type(None)):
            # convert to numpy
            if isinstance(self.raw_dataset,pd.DataFrame):
                self.raw_dataset = self.raw_dataset.to_numpy()
            if np.isnan(self.raw_dataset).any() and not self.is_corr_matrix:
                self.raw_dataset_imputated = impute_values(self.raw_dataset, how=self.impute)

        # get the correlation matrix
        if not self.is_corr_matrix:
            if not isinstance(self.raw_dataset_imputated,type(None)):
                self.correlations_matrix = np.abs(corr(self.raw_dataset_imputated))
            else:
                self.correlations_matrix = np.abs(corr(self.raw_dataset))

        # Start Calculations
        self.fa_f = FactorAnalyzer(rotation=self.rotation_fa_f,
                                   method=self.method_fa_f,
                                   is_corr_matrix=True)
        self.fa_f.fit(self.correlations_matrix)
        self.fa_g = FactorAnalyzer(rotation=None,
                                   is_corr_matrix=True,
                                   method=self.method_fa_g,
                                   n_factors=1)
        self.fa_g.fit(self.fa_f.phi_)
        # Omega Report
        self.general_component = np.dot(self.fa_f.loadings_, self.fa_g.loadings_)
        Vt = self.correlations_matrix.sum().sum()
        V = self.correlations_matrix
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
        self.lambda1 = 1 - np.diag(V).sum() / Vt
        C2 = ((V - np.eye(n) * np.diag(V)) ** 2).sum().sum()
        self.lambda2 = self.lambda1 + (n / (n - 1) * C2) ** 0.5 / Vt
        """Calculate general component. The part corresponding to the common factor  """
        general_component = np.dot(self.fa_f.loadings_,
                                   self.fa_g.loadings_)
        self.general_component_loading = np.abs(general_component)
        self.general_component_eigenvalue = np.dot(general_component.T, general_component)
        # Update Group Factors
        f_loadings_final = np.zeros(self.fa_f.loadings_.shape)
        for i in range(0, self.fa_g.get_uniquenesses().__len__()):
            f_loadings_final[:, i] = self.fa_f.loadings_[:, i] * \
                                     self.fa_g.get_uniquenesses()[i] ** 0.5
        self.f_loadings_final = np.abs(f_loadings_final)
        self.f_eigenvalues_final = np.dot(f_loadings_final.T, f_loadings_final).sum(axis=1)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)