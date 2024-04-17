# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:33:47 2024

@author: wescl
"""

import numpy as np
import pandas as pd

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

customersID = customers['id'].tolist()
ordersID = orders['customerId'].tolist()

ans = []
for x in customersID:
    if x not in ordersID:
        ans.append(x)
        
df = customers[customers['id'].isin(ans)][['name']]

df = df.rename(columns={"name":"customer"})
