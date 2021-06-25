#!/usr/bin/env python
# coding: utf-8

# code to aggregate multiple certification rank schemes

#Rank1, Rank2, Rank3, Rank4 (four ranks of four schemes structured as single list)
#'Java', 'Bigdata', 'Python', 'Cloud'
#'Java', 'Python', 'Bigdata', 'Cloud'
# likewise the other two schemes
# Weights are used to emphasize the rank positions while aggregation

# Python Libraries
import pandas as pd
import numpy as np

# RPY2
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

# Activating the environment
pandas2ri.activate()



# Setting up communication between the R and Python - 'montecarlo2.R' is the R script file
r = robjects.r
r['source']('montecarlo2.R')

# 'aggr_priorites' is the user defined function in the script 'montecarlo2.R'
rank_aggr_function_r = robjects.globalenv['aggr_priorities']



###################### Ranking aggregator application ###############################


# Input data - python data objects
certifications = ['Java', 'Bigdata', 'Python', 'Cloud', 'Java', 'Python', 'Bigdata', 'Cloud', 'Cloud','Java', 'Bigdata', 'Python']
weights = [0.418846731, 0.061132426, 0.260823588, 0.259197254, 0.418846731, 0.061132426, 0.260823588, 0.259197254, 0.418846731, 0.061132426, 0.260823588, 0.259197254]

# Convert data to R data objects
certifications_r = robjects.StrVector(certifications)
weights_r = robjects.FloatVector(weights)

# Calling R function from python
df_result_r = rank_aggr_function_r(certifications_r, weights_r)

# Converting the R's function output back to python object
df_result = pandas2ri.py2rpy(df_result_r)

