import pandas as pd 
import math
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import random

""" Loads data from Udacity Inference Statisctics Course Data Portfolio"""
df = pd.read_csv('./data/engagement-ratio.csv') 

"""Get list of columns"""

columns = df.columns.values.tolist()

column_index = 0
selected_column = columns[column_index]

""" Dataframe to Series to sampling"""
df[selected_column] = pd.to_numeric(df[selected_column], errors ='coerce')

""" Sample Size"""
n = 30

""" Find population mean and sd for hypothesis testing"""

mu = df["EngagementRatio"].mean(skipna=True)
sigma = df["EngagementRatio"].std(skipna=True)

""" Sampling """
sm = pd.read_csv('./data/engament-ratio-after-song.csv')

""" Find sample mean and standard deviation for calculate lower and upper bound depends on give confidence interval"""
xbar = sm["EngagementRatio"].mean(skipna=True)
sd = sm["EngagementRatio"].std(skipna=True)

"""  Significance Level """

sl = 0.05

""" Null Hypothesis 
    h0: mu = mean
    ha: mu != mean
"""

print('xbar: ', xbar)
print('mu: ', mu)
print('sigma: ', sigma)


zvalue = (xbar - mu) / (sigma / math.sqrt(n)) 
print('z value derived from sample: ', zvalue)

z = stats.norm.ppf(1 - sl/2)
print("z value of level of significance: ", z)

if zvalue > z:
    print('reject')
else:
    print('do not reject')

