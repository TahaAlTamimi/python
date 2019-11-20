#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:04:49 2019

@author: owner
"""
"""
num1=10.22214578
num2=10.12345678
print('num 1 is {0:.3f} and num2 is {1:.3f}'.format(num1,num2))
print(f'num 1 is {num1:.3f} and num2 is {num2:.3f}')
"""
#num=0
#age=int(input(f'your age{num+1}'))
"""
a, b = 1,10
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a = b")
"""
"""
a, b = 1,10  
max = a if (a > b) else b 
print(max)
"""
"""
if 'a' in['b','c','a']:
    print("a in the list")
else:
 print("a not in the list")
 """
"""
a=10 
b=5 
if a > b:
     print("a is greater than b")
"""
"""
a = 2
b = 330
print("A") if a > b else print("B")
"""
"""
x=int(input('num1'))
y=int(input('num2'))
if x>=y:
    print(y,x)
   
else:
   print(x,y)  
   """
   
"""
name=str(input('name'))
age=int(input('age'))
if age<18:
    print('Under Age')
    avg=int(input('your avarge'))
    if avg>=90:
     print('Exellent')
    elif avg>=50 and avg<90:
     print('Passed')
    else:
     print('Faild')
else:
    print('Adult')
    job=input('your job')
    print(age,name,job)
"""
"""
for a in range(1,6,2):
    print(a)
    """
    
"""
for a in range(10):
    print('*')    
"""
"""
for a in range(10):
    print('*',end=' ')
    """
"""
x='*'
for i in range(8):
    
    print(x*i)
    """
   
"""
x=''
s='*'
for i in range(8):
    x=x+'*'
    print('i',i)        
    for n in range(8):
     print('*'*i,n)
   
"""
"""
for i in range(10):
    for j in range(i):
        print('*',end='')

    print()
   """ 
"""  
a=8
b=0
v=""
while a>1:
    a-=1
    while b<8:
        b+=1
        print('*'*b)
    
    print('1'*a)
   
    """
"""
a=8
b=0
v=""
while a>0:
   
    while b<8:
        b+=1
        print(' '*a,end='')
        print('*'*b)
       
        a-=1
   """ 
"""
Q1

a=int(input('num1'))
b=int(input('num2'))
if a>b:
    print(a)
elif b>a:
 print(b)
else:    
 print('equal') 
  """
"""
  Q2
a=int(input('num'))
for i in range(10):
    print(i+1,'*',a,'=',(i+1)*a)
"""

# =============================================================================
# a=int(input('num'))
# b=0
# v=""
# while a>1:
#     a-=1
#     while b<5:
#         b+=1
#         print('*'*b)
#     
#     print('*'*a)
# =============================================================================

# =============================================================================
#Q4 
#letters=["x","y","z","a","b","c"]
# for i in letters:
#     if i=="a":
#         continue
#     elif i=="c":
#         break
#     print(i)
#     
# =============================================================================
# =============================================================================
# Q5
# for x in range(12,25,3):
#     print(x)
# =============================================================================
# =============================================================================
# Q6
# i=1
# while i<6:
#     print(i)
#     if i==3:
#         break
#     i+=1
# =============================================================================
# =============================================================================
# Q7
# x=0
# a=int(input('num'))
# for i in range(a):
#    x=x+i+1
# print(x)
# =============================================================================
# =============================================================================
# Q8
# a=int(input('num'))
# if a%2==0:
#     print('even')
# else:
#     print('odd')    
# 
# =============================================================================
#======================================================
#Q10 =============================================================================
# while True:
#     try:
#         a=int(input('num'))
#         break
#     except ValueError:
#         print("No valid integer! Please try again ...")
# print(a)
#         
# =============================================================================
#Q11
# Error Occured and handled 
# =======================
 
# =============================================================================
# =============================================================================
# a=10
# b=0
# v=""
# while a>1:
#       a-=1
#       while b<a-1:
#           b+=1
#           print(b,'*'*b)
#     
#       print(a,'*'*a)
# =============================================================================
      
      
      
      
#=============================================================================
# a=10
# b=0
# v=""
# while a>1:
#       a-=1
#       while b<a-1:
#           b+=1
#           print('*'*b)
#     
#       print('*'*a)
# 
# =============================================================================

# =============================================================================
# a=8
# b=0
# v=""
# while a>1:
#        a-=1
#        while b<a-1:
#            b+=1
#            print(b,'*'*b)
#      
#        print(a,'*'*a)
# while a>0:
#     while b<8:
#         b+=1
#         #print(''*b)
#         print(''*a)
#         
#        
#         a-=1
#         
# =============================================================================
    
# =============================================================================
# part1
# a=10
# b=0
# v=""
# while a>1:
#        a-=1
#        while b<a-1:
#            b+=1
#            print(b,'*'*b)
#      
#        print(a,'*'*a)
#     
# =============================================================================
    
# =============================================================================
# a=10
# b=0
# v=""
# while a>0:
#    
#     while b<8:
#         b+=1
#         print(' '*a,end='')
#         print('*'*b)
#      
#         
#        
#         a-=1
# =============================================================================
# =============================================================================
# 
# rows=5
# 
# c= 1
# for i in range(1, rows ): 
#        
#         for j in range (1, (rows - i-1) ): 
#             print(end = " ") 
#           
#       
#         while c != (2 * i ): 
#             print(c+1, end = "") 
#             c = c + 1
#         n = 0
#       
#         print()  
#   
# k = 1
# c = 1
# for i in range(1, 9): 
#     
#         for j in range (1, k ): 
#             print(end = " ") 
#         k = k + 1
#           
#         while n <= (2 * (rows - i) ): 
#             print(n, end = "") 
#             n = n + 1
#         n = 1
#         print() 
#   
# =============================================================================

n =9
c = 1
for x in range(n):
    for y in range (n-x-1):
        print(" ", end ="")
        
    for z in range (x+1):
        print(c, end="")
        c=c+1
        if z == x:
            c=c-1
            for m in range (x):
                c=c-1
                print(c,end="")
    c = 1
    print("\n", end ="")
    
for x in range(n-2,-1,-1):
    for y in range (n-1-x):
        print(" ", end ="")
        
    for z in range (x*2+1):
        if(z >= (x*2+1)//2):
            print(c, end="")
            c=c-1
        else:
            print(c, end="")
            c=c+1
       
    print("\n", end ="")
    c=1

    
    
    
    
    
    
    
    
    
    
    
    