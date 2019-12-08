#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:48:29 2019

@author: owner
"""
from flask import Flask ,render_template
app=Flask(__name__)
@app.route('/')
# =============================================================================
# @app.route('/ta/<name>')
# =============================================================================
def index():
    return render_template('Index1.html') 



    

@app.route('/hello')
# =============================================================================
# @app.route('/ta/<name>')
# =============================================================================
def hello():
    return render_template('Index2.html') 


@app.route('/members')
def member():
    return render_template('Index3.html') 
if __name__=='__main__':
    app.run(debug=True)