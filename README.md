[![DOI](https://zenodo.org/badge/445846537.svg)](https://zenodo.org/badge/latestdoi/445846537)


# OmegaPy
## Summary
Simple implementation in Python of the reliability measures: Omega Total,
Omega Hierarchical and Omega Hierarchical Total.

| Name                                                                                  | Link                                                                                                                                                                | 
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Omega Total    ![w](https://latex.codecogs.com/svg.latex?\omega_{t})                  | Tell us how muhc variance can the model explain                                                                                                                     |
| Omega Hierarchcal  ![w](https://latex.codecogs.com/svg.latex?\omega_{h})              ||
| Omega Hierarchycal Limit ![w](https://latex.codecogs.com/svg.latex?\omega_{h_{\infty}}) | |


## Context
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
