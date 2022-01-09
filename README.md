[![DOI](https://zenodo.org/badge/445846537.svg)](https://zenodo.org/badge/latestdoi/445846537)

# ReliabiliPy

## Summary
Simple implementation in Python of the [reliability](https://en.wikipedia.org/wiki/Reliability_(statistics)) measures for surveys: Omega Total,
Omega Hierarchical and Omega Hierarchical Total.

| Name                                                                                                                    | Link                                                                                                                                                                | 
|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Omega Total    ![w](https://latex.codecogs.com/svg.latex?\omega_{t})                                                    | Tell us how muhc variance can the model explain                                                                                                                     |
| Omega Hierarchcal  ![w](https://latex.codecogs.com/svg.latex?\omega_{h})                                                ||
| Omega Hierarchycal Limit ![w](https://latex.codecogs.com/svg.latex?\omega_{h_{\infty}})                                 | |
| [Cronbach's alpha](https://en.wikipedia.org/wiki/Cronbach%27s_alpha)  ![w](https://latex.codecogs.com/svg.latex?\alpha) | |


See [Documentation](https://rafaelvalero.github.io/OmegaPy/)
## Quick Start

```python
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
print('here omega Hierarchical: ', reliability_report.omega_hierarchical)
print('here Omega Hierarchical infinite or asymptotic: ', reliability_report.omega_hierarchical_asymptotic)
print('here Omega Total', reliability_report.omega_total)
print('here Alpha Cronbach total', reliability_report.alpha_cronbach)
```

# Context
It is common to try check the [reliability](https://en.wikipedia.org/wiki/Reliability_(statistics)), i.e.: the consistency of 
a measure, particular in psychometrics and surveys analysis. 

 `R` has packages for this kind of analysis available, such us `psych`by Revelle (2017). `python` goes behind on this.
The closes are [factor-analyser](https://github.com/EducationalTestingService/factor_analyzer) and [Pingouin](https://pingouin-stats.org/index.html).
As I write this there is a gap in the market since none of the above libraries currently implement any 
 omega related reliability measure. Although Pingouin implements [Cronbach's alpha](https://en.wikipedia.org/wiki/Cronbach%27s_alpha)

# References
* Flora, David B. "Your coefficient alpha is probably wrong, but which coefficient omega is right? A tutorial on using R to obtain better reliability estimates." Advances in Methods and Practices in Psychological Science 3.4 (2020): 484-501. https://journals.sagepub.com/doi/pdf/10.1177/2515245920951747 
* Revelle, Willian. Manuscrip. 2021. An introduction to psychometric theory with applications in R.
https://personality-project.org/r/book/Chapter7.pdf 
* Revelle, William R. "psych: Procedures for personality and psychological research." (2017). 
    * Omega Implementation in R. https://github.com/cran/psych/blob/master/R/omega.R
    * Schmid-Leiman in R. https://github.com/cran/psych/blob/master/R/schmid.R 
* Starkweather, Jon (2013). Hierarchical Factor Analysis. https://it.unt.edu/sites/default/files/hierfa_l_jds_apr2013.pdf
* Vallat, R. (2018). Pingouin: statistics in Python. Journal of Open Source Software, 3(31), 1026, https://doi.org/10.21105/joss.01026
* Wolff, Hans-Georg, and Katja Preising. "Exploring item and higher order factor structure with the Schmid-Leiman solution: Syntax codes for SPSS and SAS." Behavior Research Methods 37.1 (2005): 48-58.

# Acknowledgement
* real-statistics.com
* Factor Analyzer. Python library. https://github.com/EducationalTestingService/factor_analyzer 
