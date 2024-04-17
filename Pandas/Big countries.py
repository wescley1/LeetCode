# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:37:17 2024

@author: wescl
"""



import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
 
# Loading irirs dataset
data = pd.read_csv("countries.csv")
#data = load_iris()
world = pd.DataFrame(data, columns=["name","continent","area","population","gdp"])

df = world.loc[(world["population"]>=25000000) | (world["area"]>=3000000)]
res = df[['name','area','population']]

display(df)
