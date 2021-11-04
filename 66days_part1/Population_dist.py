# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

to do:
    - Make a normal distribution myself
    - Turn this into a simulation / potentially interactive

"""

import random 
import matplotlib.pyplot as plt
import numpy as np


# day 1:
    
# I want to make a random population

# method 1 use numpy array
population_size = 1000
mean = 6
strd_dev = 2
population = np.random.normal(loc=mean, scale=strd_dev, size=population_size)

# plot that population
plt.hist(population, density=False, bins=30)  # density=True would provide probability
plt.ylabel('count')
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
    
# take a smaple from that population 
# where I can alternate n

# day 3: create different types of distributions
# 

