import pandas as pd
import numpy as np
from reliabilipy import reliability_analysis
from nose.tools import raises

def test_case_presing_et_all_2002():
    """
    In this notebook I try to replicate Wolff and Preising 2005 in Python and I would compare in R, too.

    * Wolff, Hans-Georg, and Katja Preising. "Exploring item and higher order factor structure with the Schmid-Leiman solution: Syntax codes for SPSS and SAS." Behavior Research Methods 37.1 (2005): 48-58.

    Data:
    * Moser, K., Preising, K., Göritz, A. S., & Paul, K. (2002). Steigende Informationsflut am Arbeitsplatz: Belastungsgünstiger Umgang mit elektronischen Medien

    Results checked on R.
    """

    correlations_matrix = pd.DataFrame(np.array([[1., 0.483, 0.34, 0.18, 0.277, 0.257, -0.074, 0.212, 0.226],
                                          [0.483, 1., 0.624, 0.26, 0.433, 0.301, -0.028, 0.362, 0.236],
                                          [0.34, 0.624, 1., 0.24, 0.376, 0.244, 0.233, 0.577, 0.352],
                                          [0.18, 0.26, 0.24, 1., 0.534, 0.654, 0.165, 0.411, 0.306],
                                          [0.277, 0.433, 0.376, 0.534, 1., 0.609, 0.041, 0.3, 0.239],
                                          [0.257, 0.301, 0.244, 0.654, 0.609, 1., 0.133, 0.399, 0.32],
                                          [-0.074, -0.028, 0.233, 0.165, 0.041, 0.133, 1., 0.346, 0.206],
                                          [0.212, 0.362, 0.577, 0.411, 0.3, 0.399, 0.346, 1., 0.457],
                                          [0.226, 0.236, 0.352, 0.306, 0.239, 0.32, 0.206, 0.457, 1.]]))
    reliability_report = reliability_analysis(correlations_matrix=correlations_matrix)
    reliability_report.fit()
    np.testing.assert_almost_equal(reliability_report.omega_hierarchical, 0.5451484335574861, decimal=3)
    np.testing.assert_almost_equal(reliability_report.omega_total, 0.8579745972600469, decimal=3)
    np.testing.assert_almost_equal(reliability_report.omega_hierarchical_asymptotic, 0.6353899466236236, decimal=3)
    np.testing.assert_almost_equal(reliability_report.alpha_cronbach, 0.803183205136355, decimal=3)
    np.testing.assert_almost_equal(reliability_report.lambda1, 0.7139, decimal=3)
    np.testing.assert_almost_equal(reliability_report.lambda2, 0.8149701194973398, decimal=3)


def test_case_revelle_chapter7():
    """
    Dataset as examample in Table 7.5
     https://personality-project.org/r/book/Chapter7.pdf
    Results are checked in that pdf.
    """

    correlations_matrix = pd.DataFrame(np.array([[1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
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
    reliability_report = reliability_analysis(correlations_matrix=correlations_matrix)
    reliability_report.fit()
    np.testing.assert_almost_equal(reliability_report.omega_hierarchical, 0.541353, decimal=3)
    np.testing.assert_almost_equal(reliability_report.omega_total, 0.902255, decimal=3)
    np.testing.assert_almost_equal(reliability_report.omega_hierarchical_asymptotic, .600000, decimal=3)
    np.testing.assert_almost_equal(reliability_report.alpha_cronbach, 0.844839, decimal=3)
    np.testing.assert_almost_equal(reliability_report.lambda1, 0.7744360, decimal=3)
    np.testing.assert_almost_equal(reliability_report.lambda2, 0.85374, decimal=3)

@raises(ValueError)
def test_analyze_impute_value_error():
    ra = reliability_analysis(impute='blah',
                              correlations_matrix=np.random.randn(500).reshape(100, 5))
    ra.fit()


@raises(ValueError)
def test_analyze_methods_g_value_error():
    ra = reliability_analysis(method_fa_g='blah',
                              correlations_matrix=np.random.randn(500).reshape(100, 5))
    ra.fit()

@raises(ValueError)
def test_analyze_methods_f_value_error():
    ra = reliability_analysis(method_fa_f='blah',
                              correlations_matrix=np.random.randn(500).reshape(100, 5))
    ra.fit()

@raises(ValueError)
def test_analyze_rotation_fa_f_value_error():
    ra = reliability_analysis(rotation_fa_f='blah',
                              correlations_matrix=np.random.randn(500).reshape(100, 5))
    ra.fit()