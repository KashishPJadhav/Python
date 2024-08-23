# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:02:27 2024

@author: DELL
"""

import pandas as pd
df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
print(df.isnull())
df.dropna(inplace=True)
print("Using dropna")
print(df)
df = pd.DataFrame({'A': [10, 20, None], 'B': [40, None, 60]})
print("Using fillna")
df.fillna(0, inplace=True)
print(df)
