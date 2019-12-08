#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:19:08 2019

@author: owner
"""

import sqlite3
conn = sqlite3.connect('OrgDB.db')
c = conn.cursor()
c.execute('''CREATE TABLE OrgDB
          (EmployeeNumber int, EmployeeName text, EmployeeGender text, EmployeeNationality text, EmployeeDateofBirth text , EmployeeAddress text, EmployeeDepartment text , EmployeeSalary real)''')




conn.commit()
conn.close()




