#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:53:05 2019

@author: owner
"""

# Exercise =============================================================================
# class Employee:
#     
#     def __init__(self,num,name,adress,salary,jobtitle):
#         self.numpublic=int(num)
#         self.__nameprivate=str(name)
#         self.__adressprivate=str(adress)
#         self.__salaryprivate=float(salary)
#         self.__jobtitleprivate=str(jobtitle)
#         
#         
#     def getnum(self):
#             return self.numpublic
# 
#     def getname(self):
#         return self.__nameprivate
#     
#     def getadress(self):
#         return self.__adressprivate
#     
#     def setadress(self,adress):
#            self.__adressprivate=adress
# 
# 
#     def getsalary(self):
#         return self.__salaryprivate
#     
#     def getjobtitle(self):
#         return  self.__jobtitleprivate
#      
# 
#     def __del__(self): 
#         print (self.__nameprivate+ ' have been deleted')
#         
#     def info(self): 
#         print('Employee information : ',self.numpublic)
#         print('Employee number: ',self.numpublic)
#         print('Name: ',self.__nameprivate)
#         print('adress: ',self.__adressprivate)
#         print('salary: ',self.__salaryprivate)
#         print('job Tiltle: ',self.__jobtitleprivate)
#        
#     def info2(self):
#             print('Employee information : ',self.numpublic,end='')
#             print(', Employee number: ',self.numpublic,end='')
#             print(' , Name: ',self.__nameprivate,end='')
#             print(' , adress: ',self.__adressprivate,end='')
#             print(' , salary: ',self.__salaryprivate,end='')
#             print(', job Tiltle: ',self.__jobtitleprivate)
#         
# emp=Employee
# emp1= Employee(1,'mohammad khalid','amman,jordan',500,'consulant')
# emp2= Employee(2,'hala rana','aqab,jordan',750,'manager')
# 
# emp1.setadress('USA')
# emp1.info()
# emp1.info2()
# del emp1
# del emp2
# =============================================================================






# =============================================================================
# class Person :
#     def say_hello(x):
#         
#         print('Hello')
#     
# p = Person()
# p.say_hello()
# =============================================================================

# =============================================================================
# class Person:
#     # constructor or initializer
#         def __init__(self, name): 
#             self.name = name
#         
#         # method which returns a string
#         def whoami( self):
#             return "I am " + self.name
#         # destructors 
#         def __del__( self):
#             print ( 'I have been deleted '+ self.name)
#            
#             
# p1 = Person('issa') 
# print(p1.whoami())
# print(p1.name)
# del p1
# 
# =============================================================================

# =============================================================================
# class Encapsulation():
#     def __init__(self, a, b, c):
#         self.Apublic= a 
#         self._Bprotected= b
#         self.__Cprivate= c
#     def getprivate(self):
#             return self.__Cprivate 
#         
#     def setprivate(self,ace):
#           self.__Cprivate=ace
# # =============================================================================
# #           return 'you are added True:'
# # =============================================================================
#         
# x = Encapsulation(11,13,17)
# print ( x.Apublic)
# print ( x._Bprotected)
# #print ( x.__Cprivate) error 
# ( x.setprivate(7))
# print ( x.getprivate()) 
#  
# =============================================================================
# =============================================================================
# class Parent(object):
#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age = age
#         self.__salary = salary
#         
#     def public(self):
#         print("calling public")
#         
#     def _protected(self):
#         print("calling protected")
# 
#     def __private(self):
#         print("is it really private?")   
#         
# class Child(Parent):
#     def foo(self):
#         self.public()
#         self._protected()
#         print(self.name)
#         print(self._age)
#         print(self.__salary)
#         
# c = Child('ah',40,50)
# c.foo()
# c.public()
# =============================================================================

# =============================================================================
# 
# class MySuperClass1():
#     def method_super1(self):
#         print("method_super1 method called")
# class ChildClass(MySuperClass1):
#     def child_method(self):
#         print("child method")
# c = ChildClass()
# c.method_super1()
# c.child_method()
# =============================================================================

# =============================================================================
# class MySuperClass1():
#     def method_super1(self):
#         print("method_super1 method called")
# class MySuperClass2():
#     def method_super2(self):
#         print("method_super2 method called")
# class ChildClass(MySuperClass1, MySuperClass2 ):
#     def child_method(self):
#         print("child method")
#         
# c = ChildClass()
# c.method_super1()
# c.method_super2()
# c.child_method()
# 
# 
# =============================================================================

# =============================================================================
# class Circle:
#     def __init__(self, radius):
#         self.__radius= radius 
#     def setRadius(self, radius):
#             self.__radius= radius 
#     def getRadius(self): 
#                 return self.__radius 
#     def __add__(self, another_circle):
#                 
#           return Circle( self.__radius+ another_circle.__radius)
# c1 = Circle(4)
# print(c1.getRadius())
# c2 = Circle(5)
# print(c2.getRadius())
# c3 = (c1 + c2)
# print(c3.getRadius())
# =============================================================================



# x = Encapsulation(11,13,17)
# print ( x.Apublic)
# print ( x._Bprotected)
# #print ( x.__Cprivate) error 
# ( x.setprivate(7))
# print ( x.getprivate())














