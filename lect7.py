#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:06:14 2019

@author: owner
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# Q1=============================================================================
# data = [2, 4, 6, 8, 10]
# s = pd.Series(data)
# print(s)
# 
# =============================================================================

#Q2 =============================================================================
# d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
# 
# d=pd.Series(d1)
# 
# print(d)
# =============================================================================
# Q3=============================================================================
# data = [20, 10, 150, 110, 100, 50]
# s = pd.Series(data)
# 
# print( s.describe())
# s.plot(kind="bar")
# =============================================================================

# Q4=============================================================================
# data = {'d1':[100,200,5,400,700,100,200,50,400,700],
#         'd2':[140,0,300,400,200,140,0,700,400,200]}
# 
# df=pd.DataFrame(data,columns=['d1','d2'])
# print(df)
# print( df.describe())
# df.plot()
# =============================================================================

#Q5 =============================================================================
# data={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
# df=pd.DataFrame(data)
# print(df)
# =============================================================================

#Q6 =============================================================================
# names = ['Bob','Jessica','Mary','John','Mel']
# births = [968, 155, 77, 578, 973]
# 
# series = pd.Series(births, index=names, name='series')
# 
# print(series)
# 
# 
# 
# series.plot.pie(y='births', figsize=(5, 5),)
# =============================================================================
#Q7 =============================================================================
# import pandas as pds
# d = [100,2200,300,400,500,600,700,800,900]
# df= pds.DataFrame(d, columns = ['Number'])
# df.to_csv('panda.csv', sep='\t')
# df= pds.read_csv('panda.csv',sep='\t',index_col=0)
# print(df)
# =============================================================================

# =============================================================================
# print( df.describe())
# =============================================================================
# Q8=============================================================================
# dates =pd.date_range('20000101', periods=4)
# df= pd.DataFrame(np.random.randn(4, 2), index=dates, columns=["A","B"])
# print(df)
# print(df.head(2))
# print(df[['A']])
# print(df[0:1])
# print(df['20000102':'20000104'])
# print(df.loc['20000102':'20000104', ["A"]])
# print(df.iloc[:,1:2])
# print(df[df>0])
# print(df[df.B>0])
# df["A"]=[100,200,300,100]
# print(df)
# print(df[df['A'].isin([200,300])])
# 
# =============================================================================






# =============================================================================
# 
# data = [100, 120, 140, 180, 200, 210, 214]
# s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# print(s)
# print('the head',s.head(3))
# 
# print( s.describe())
# 
# print( s.agg(['sum','max','mean','std']))
# =============================================================================
# =============================================================================
# data = {'apples': [3, 2, 0, 1], 'oranges': [0, 3, 7, 2]}
# purchases = pd.DataFrame(data)
# print ( purchases ) 
# print ( purchases.describe() )
# =============================================================================
# =============================================================================
# 
# dates = pd.date_range('20190101', periods=8)
# df= pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))
# print(df.head(),'\n','we')
# print(df['P'])
# =============================================================================
# =============================================================================
# dates = pd.date_range('20190101', periods=8)
# df= pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))
# print(df.head())
# print(df[['P','Q']])
# 
# df.to_excel('PandaTest2.xlsx', sheet_name= 'testing', index = True)
# df.to_csv('myDataFrame2.csv', sep='\t')
# =============================================================================
# =============================================================================
# d = [1,2,3,4,5,6,7,8,9]
# df= pd.DataFrame(d, columns = ['Number'])
# df.to_excel('PandaTest.xlsx', sheet_name= 'testing', index = True)
# df.to_csv('myDataFrame.csv', sep='\t')
# =============================================================================
