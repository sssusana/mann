#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 19:14:51 2018

@author: Susana
"""

############## Two Sample T-Test and Mann Whitney Analysis ##############

print("T test and Mann Whitnet Analysis for 2 samples" )

#importing packages
import csv
import os
import sys
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu, normaltest, shapiro

#def dir
os.chdir("/Users/Susana/Documents/GitHub/mann")

#load data
data = np.array([
[6.61, 1], 
[6.49, 1],
[8.53, 1],
[7.35, 1],
[6.80, 1],
[6.41, 1],
[8.39, 1],
[5.92, 1],
[4.35, 1],
[4.05, 1],
[7.16, 0],
[6.95, 0],
[8.08, 0],
[7.02, 0],
[6.44, 0],
[6.38, 0],
[7.99, 0],
[6.33, 0],
[5.06, 0],
[3.59, 0]])



#normality tests

ntest = normaltest(data)
print(ntest)

shawil = shapiro(data)
print(shawil) 

 
#slice the groups (masc = 0; fem= 1)
masc = data[:, 1] == 0
masc = data[masc][:, 0]
fem = data[:, 1] == 1
fem = data[fem][:, 0]

#TSTUDENT 
t_statistic_t2, p_value_t2 = ttest_ind(masc, fem)
a
print "Resultado para Análise Two-Sample T-Test", p_value_t2


#Mann-whitney
p_value_m2 = mannwhitneyu(masc, fem)
print "Resultado para Análise Mann Whitney", p_value_m2



