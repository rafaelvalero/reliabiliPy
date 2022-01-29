[![DOI](https://zenodo.org/badge/445846537.svg)](https://zenodo.org/badge/latestdoi/445846537)

# reliabiliPy

## Summary 
* Simple  implementation in Python of the [reliability](https://en.wikipedia.org/wiki/Reliability_(statistics) measures for surveys: Omega Total,
Omega Hierarchical and Omega Hierarchical  Asymptotic and Omega Total, using Schmid-Leiman solution. 
* Also Cronbach's Alpha Guttman’s lower bounds of reliability $\lamda_1$ and  $\lamda_2$.
* Explanations  and documentation  available

See [Documentation](https://rafaelvalero.github.io/reliabiliPy/)
## Quick Start

If you have the correlations matrix of your dataset.

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
print(reliability_report.lambda1)
print(reliability_report.lambda2)
print(reliability_report.report_eigenvalues)
print(reliability_report.report_loadings)

```

If you want to use the whole dataset you could do it to, adding the inputations method
you prefer:

```python
import pandas as pd
import numpy as np
from reliabilipy import reliability_analysis
raw_dataset = pd.DataFrame([{'C1': 2.0, 'C2': 3.0, 'C3': 3.0, 'C4': 4.0, 'C5': 4.0},\
        {'C1': 5.0, 'C2': 4.0, 'C3': 4.0, 'C4': 3.0, 'C5': 4.0},\
        {'C1': 4.0, 'C2': 5.0, 'C3': 4.0, 'C4': 2.0, 'C5': 5.0},\
        {'C1': 4.0, 'C2': 4.0, 'C3': 3.0, 'C4': 5.0, 'C5': 5.0},\
        {'C1': 4.0, 'C2': 4.0, 'C3': 5.0, 'C4': 3.0, 'C5': 2.0},\
        {'C1': 4.0, 'C2': np.nan, 'C3': 3.0, 'C4': 5.0, 'C5': 5.0},\
        {'C1': np.nan, 'C2': 4.0, 'C3': 5.0, 'C4': 3.0, 'C5': 2.0}])
ra = reliability_analysis(raw_dataset=raw_dataset,
                              is_corr_matrix=False,
                              impute='median')
ra.fit()
print('here omega Hierarchical: ', ra.omega_hierarchical)
print('here Omega Hierarchical infinite or asymptotic: ', ra.omega_hierarchical_asymptotic)
print('here Omega Total', ra.omega_total)
print('here Alpha Cronbach total', ra.alpha_cronbach)
```

# Context
It is common to try check the [reliability](https://en.wikipedia.org/wiki/Reliability_(statistics)), i.e.: the consistency of 
a measure, particular in psychometrics and surveys analysis. 

`R` has packages for this kind of analysis available, such us `psych`by Revelle (2017). `python` goes behind on this.
The closes are [factor-analyser](https://github.com/EducationalTestingService/factor_analyzer) and [Pingouin](https://pingouin-stats.org/index.html).
As I write this there is a gap in the market since none of the above libraries currently implement any 
omega related reliability measure. Although Pingouin implements [Cronbach's alpha](https://en.wikipedia.org/wiki/Cronbach%27s_alpha)

## Aim
1. To bring functions to ```python``` for psychometrics and survey analysis, as there is a gap. Mostly from the package in `R` `psych`.
2. To make the ideas and math behind those clear and transparent with examples, and documentation.
3. To allow people to collaborate and ask questions about.

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

## Acknowledgement
* Factor Analyzer. Python library. This library is based heavily on this one. https://github.com/EducationalTestingService/factor_analyzer 

# Cite this package as
* Rafael Valero Fernández. (2022). reliabiliPy: measures of survey domain
reliability in Python with explanations and examples. 
Cronbach´s Alpha and Omegas. (v0.0.0). 
Zenodo. https://doi.org/10.5281/zenodo.5830894

or
```bibtex
@software{rafael_valero_fernandez_2022_5830894,
  author       = {Rafael Valero Fernández},
  title        = {{reliabiliPy: measures of survey domain reliability 
                   in Python with explanations and examples.
                   Cronbach´s Alpha and Omegas.}},
  month        = jan,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {v0.0.0},
  doi          = {10.5281/zenodo.5830894},
  url          = {https://doi.org/10.5281/zenodo.5830894}
}
```
Happy to modify the above as petition and contributions.