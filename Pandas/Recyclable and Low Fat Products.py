# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:25:20 2024

@author: wescl
"""
import pandas as pd

products = pd.read_csv("products.csv")

df = products.loc[(products["low_fats"]=="Y") & (products["recyclable"]=="Y")]
df = df[['product_id']]

display(df)