# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 21:38:12 2021

@author: bhave
"""
import pandas as pd

data =  pd.read_csv("G:/My Drive/Exams/Data analytics applications/github/daa_2021s2/Exercises/05 Classification/Datasets/spambase.data", sep=",", header=None)
print(data)

data.to_csv("G:/My Drive/Exams/Data analytics applications/github/daa_2021s2/Exercises/05 Classification/Datasets/spambase.csv")