#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:53:47 2019

@author: owner
"""

# =============================================================================
# x = "awesome"
# def myfunc():
#     global x
#     x = "fantastic"
#     print("Python is " + x)
# myfunc()
# print("Python is " + x)
# =============================================================================
# =============================================================================
# def factorial(n):
#     if n == 1:
#         return 1 
#     else:
#         return n*factorial(n-1)
#     
# print(factorial(10))
# =============================================================================

# =============================================================================
# MyList= [0,1,2,3,4,10,13,22,25,100,120]
# print("squared List:", list(map(lambda x: x**2, MyList)) )
# =============================================================================
# =============================================================================
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# data=list(filter(lambda x: x > 75,scores))
# print(data)
# =============================================================================

# =============================================================================
# my_strings= ['a', 'b', 'c', 'd', 'e']
# my_numbers= [1,2,3,4,5]
# my_strings1= ['z', 'y', 'x']
# results = list(zip(my_strings, my_numbers,my_strings1))
# print(results)
# =============================================================================

# =============================================================================
# q1:
#     1-6
#     2-15
#     3-33
# =============================================================================
# =============================================================================
# Q2 
#def factorial(n):
#     if n == 1:
#         return 1 
#     else:
#        return n * factorial(n-1)
#         
# factorial(10)
# =============================================================================

#Q3 =============================================================================
# mult=lambda a,b:(a*b)
# print(mult(5,5))
# =============================================================================
# from functools import reduce
# mult=reduce (lambda a,b:a*b,[1,2,3,4,5])
# print (mult)
# 
# =============================================================================
# =============================================================================

#Q4 =============================================================================
# neg = list( filter(lambda x: x < 0 , range(-5,5)))
# print(neg)
# =============================================================================

# =============================================================================
# Q5-13
# =============================================================================

#Q6 =============================================================================
# [('joey','chandler','David'),(Monica,pheoble,rachel)]
# =============================================================================

#Q7 =============================================================================
# {(Bitcoin,BTC),(ether,eth),(ripple,xrp),(litecoin,ltc)}
# =============================================================================

#Q8 =============================================================================
# ['e', 'o']
# =============================================================================

# Q9:
# [1, 20, 10]
# =============================================================================
# =============================================================================
# Q10:
# [1, 4, 9, 16]
# =============================================================================
# =============================================================================
# Q11:
# [3, 6, 8]
# =============================================================================
# =============================================================================
# Q12:
# [6, 8]
# =============================================================================
# =============================================================================
# Q13:
# [4,6,8]
# =============================================================================
# =============================================================================
# Q14:
# list1 = [1, 3, 5, 6, 2]
# print (reduce(lambda a,b : a if a < b else b,list1))
# =============================================================================
# =============================================================================
# Q15:
# numbers= [1,2,3]
# letters=['a','b','c']
# print(list(zip(numbers, letters)))
# =============================================================================
def area(r):
    a=3.142*r**2
    print(a)
    return a 
    
    
def vol(area,l):
    print(a*l)
     
    
r=int(input('rnter raduis'))
l=int(input('length'))
a=area(r) 
vol(area,l)   































