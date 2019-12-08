#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:08:00 2019

@author: owner
"""
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.colorchooser import * 

# =============================================================================
# import sqlite3
# conn = sqlite3.connect('OrgDB.db')
# 
# c = conn.cursor()
# 
# conn.commit()
# 
# for row in c.execute('SELECT EmployeeNumber,EmployeeName FROM OrgDB '):
#     print (Label(text='row[0]').place(x=30,y=90))
#     print (row[1])
# conn.close()
# =============================================================================
win=Tk()
screen_width=win.winfo_screenwidth()
screen_height=win.winfo_screenheight()
w="500x500+"+str(int((screen_width-500)/2))+"+"+str(int((screen_height-500)/2))
win.geometry(w)
txt=scrolledtext.ScrolledText(win,width=40,height=10)
import sqlite3
conn = sqlite3.connect('OrgDB.db')

c = conn.cursor()

# =============================================================================
# c.execute('DELETE FROM OrgDB WHERE EmployeeName="aisa"  ')
# =============================================================================
txt=scrolledtext.ScrolledText(win,width=40,height=10,wrap=WORD)
txt.grid(column=0,row=1)
for row in c.execute('SELECT EmployeeNumber,EmployeeName FROM OrgDB '):
        txt.insert(END, "The count is "+ str(row[1]) + "\n")
#Pushes the scrollbar and focus of text to the end of the text input.
        txt.yview(END)
        txt.pack()

for row in c.execute('SELECT EmployeeNumber,EmployeeName FROM OrgDB '):
  print (row[1])
  
 
conn.commit()
conn.close()

# =============================================================================
# c.execute("INSERT INTO OrgDB VALUES (3, 'moh', 'male', 100,'05/23/1995','amman-jordan','coding',400)")
# =============================================================================
# =============================================================================
# print(c.execute('SELECT * FROM OrgDB ').rowcount)
# rows=c.fetchall()
# print(len(rows))
# 
# =============================================================================























# =============================================================================
# import sqlite3
# conn = sqlite3.connect('stocks.db')
# c = conn.cursor()
# c.execute('SELECT symbol,qty,price FROM stocks ORDER BY price')
# # =============================================================================
# # for row,index in enumerate(c):
# #     print ('num=',row,index)
# # =============================================================================
# print(c.fetchall())    
# conn.close()
# =============================================================================

# =============================================================================
# import sqlite3
# conn = sqlite3.connect('stocks.db')
# c = conn.cursor()
# for row in c.execute('SELECT price FROM stocks ORDER BY price'):
#     print (row)
# conn.close()
# =============================================================================

# =============================================================================
# import sqlite3
# conn = sqlite3.connect('stocks.db')
# c = conn.cursor()
# 
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'Apple', 100,35.14)")
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'Apple', 50,35.25)")
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'Aplle', 50,35.25)")
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'Aplle', 50,35.25)")
# conn.commit()
# conn.close()
# 
# =============================================================================
# =============================================================================
# import sqlite3
# conn = sqlite3.connect('stocks.db')
# c = conn.cursor()
# c.execute('DELETE from stocks where symbol = "Apple" and price=35.14')
# conn.commit()
# for row in c.execute('SELECT symbol, qty, price FROM stocks ORDER BY price'):
#     print (row)
# conn.close()
# =============================================================================
