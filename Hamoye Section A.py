import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy import * # To import all functions of numpy with having to use np.array, We can simply use array
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt


'''To generates array separated by certain differnce:'''
first= arange(1,101,3)
'''i.e 1 means start, 101 means and 3 is the differnce between numbers between 1 & 101'''
print("First array = ",first)

second= zeros(10)
print("Second array = ",second)

third= ones([3,3])
print("Third array = ",third)


'''To find the dimension of a numpy, we use shape'''
dimension= np.shape(first)
print('Dimension of first array',dimension)
'''We can then modify this to find the total elements in first array'''
print('Total elemets in first array = ', len(first))

'''To make the numpy a singular matrix i.e all rows are equal to 1 and other equal to zero'''

a=[3,31,44,2,23,27]
b=[3,11,47,23,23,87]
c=[89,1,43,20,13,7]
fourth=np.array([a,b,c])
fifth= np.eye(5)
print('Fifth array = ', fifth)
print('Fourth array = ', fourth)

'''To find the data type of a numpy array, you use dtype'''
print("First array data type = ",first.dtype)
print("Second array data type = ",second.dtype)
print("Third array data type = ",third.dtype)
print('Fourth array data type = ', fourth.dtype)
print('Fifth array data type = ', fifth.dtype)

'''For example: first array datatype means integer of 32 bits
And fifth array datatype means float of 64 bits'''







dataset = pd.read_csv('fuel_ferc1.csv')


print('Missing values: ',dataset.isnull().sum())

print('Describe: ',dataset.describe())

dataset2= dataset.describe()
dataset2.to_csv('Describe1.csv')

print('Skew:',dataset.skew())
print('kurtosis:', dataset.kurtosis())
print('correlation:', dataset.corr())


dataset3 = dataset.corr()
dataset3.to_csv('Describe2.csv')

print('Average: ',dataset.mean().min())

dataset4 = dataset.mean()
















