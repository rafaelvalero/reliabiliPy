import pandas as pd
import numpy as np
from reliabilipy import reliability_analysis
correlations_matrix = pd.DataFrame(np.matrix([[1., 0.483, 0.34, 0.18, 0.277, 0.257, -0.074, 0.212, 0.226],
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


