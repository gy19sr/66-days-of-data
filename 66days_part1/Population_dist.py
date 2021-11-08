# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

to do:
    - Make a normal distribution myself
    - Turn this into a simulation / potentially interactive

"""

import pandas as pd
import seaborn as sns
import scipy.stats as stats
import numpy as np
import random
import warnings
import matplotlib.pyplot as plt
import numpy.ma as ma


# day 1:
    
# I want to make a random population

# method 1 use numpy array
population_size = 1000
mean = 6
strd_dev = 2
population = np.random.normal(loc=mean, scale=strd_dev, size=population_size)

# plot that population
plt.hist(population, density=False, bins=30)  # density=True would provide probability
plt.ylabel('Count')
plt.xlabel('Data')


# method 2: make it myself by looking at the numpy code


# and calculate the mean strd dev and variance of that pop
str_dev_tot = 0
pop_mean = population.mean() # cheating a bit here

for i in population:
    temp = (i - pop_mean)**2
    str_dev_tot += temp
variance = (str_dev_tot/len(population))
strd_dev = (str_dev_tot/len(population)) **0.5
    

print('population mean = ', pop_mean)
print('population strd dev =', strd_dev)
print('population variance = ', variance)


#### day 2:
    
# take a sample from that population 
# where I can alternate n


### day 3: Make Confidence Intervals
# so start with 95% CI
# two tailed and one tailed
# 95% = + - 1.96 sigma
# now how to calculate this on the fly

# this works if you want to know the probability
def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2*np.pi)
    return(constant * np.exp((-x**2) / 2.0) )



CI_upper = strd_dev * 1.96 # z-table this is the value for 0.025 CL 
CI_lower = strd_dev * -1.96
# so this assumes two tail
print("Upper Confidence Interval = ", CI_upper)
print("Lower Confidence Interval = ", CI_lower)



# Make everything outside confidence intervals red

# Done with new graph


# day 4: Take random sample from the population

# plot sample distribution



# day : create different types of distributions
# 

