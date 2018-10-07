#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 11:15:20 2018

@author: yashkumararora
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import Image, display 
train = pd.read_csv('train.csv')
display(train.head())
train = train.set_index('PassengerId')
test = pd.read_csv('test.csv')
display(test.head())
train.shape
train.head()

datadict = pd.DataFrame(train.dtypes)
datadict

datadict['MissingVal'] = train.isnull().sum()
datadict

datadict['NUnique']=train.nunique()
datadict

datadict['Count']=train.count()
datadict

datadict = datadict.rename(columns={0:'DataType'})
datadict

train.describe(include=['object'])

train.describe(include=['number'])

train.Survived.value_counts(normalize=True)

figbi, axesbi = plt.subplots(2, 2, figsize=(16, 10))
train.groupby('Pclass')['Survived'].mean().plot(kind='barh',ax=axesbi[0,0],xlim=[0,1])
train.groupby('Sex')['Survived'].mean().plot(kind='barh',ax=axesbi[0,1],xlim=[0,1])
sns.boxplot(x="Survived", y="Age", data=train,ax=axesbi[1,0])
sns.boxplot(x="Survived", y="Fare", data=train,ax=axesbi[1,1])
'''
Summary
1: We can clearly visualize that male survial rates is around 20% where as female survial rate is about 75% which suggests that gender has a strong relationship with the survival rates.
2: There is also a marginal relationship between the fare and survial rate.
3: There is also a clear relationship between Pclass and the survival by referring to first plot below. Passengers on Pclass1 had a better survial rate of approx 60% whereas passengers on pclass3 had the worst survial rate of approx 22%
4. There is also a clear relationship between the age of the passengers i.e. children are given more preference than adults
5: I have quantified the above relationships further in the last statsical modelling section
'''