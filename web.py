#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:06:58 2019

@author: owner
"""


from flask import Flask,render_template
import sqlite3 as sql

DATABASE='database22.db'
app=Flask(__name__)
@app.route('/')
def index():
    with sql.connect(DATABASE) as con:
        cur=con.cursor()
    res=cur.execute('select * from users')
    return render_template('index6.html',users=res)

if __name__=='__main__':
    app.run(debug=True)