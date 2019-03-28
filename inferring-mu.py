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
n = 35

""" Find population mean for control"""

mu = df[selected_column].mean(skipna=True)

""" Sampling """
sm = df.sample(n=n)

""" Find sample mean and standard deviation for calculate lower and upper bound depends on give confidence interval"""
mean = sm[selected_column].mean(skipna=True)
sd = sm[selected_column].std(skipna=True)

""" Determine confidence interval """
ci = 0.95

""" Find z-value for given ci"""
z = stats.norm.ppf(ci)

""" Calculate margin of error """
moe = z * (sd / math.sqrt(n))

""" Calculate lower and upper bound"""
lower = mean - moe 
upper = mean + moe


print(f'We are {ci} confident population mean lies between {lower} and {upper}')
print(f'True mean is {mu}')


