#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:41:35 2019

@author: owner
"""
from flask import Flask ,render_template
app=Flask(__name__)
@app.route('/')
# =============================================================================
# @app.route('/ta/<name>')
# =============================================================================
def index():
    return render_template('Index5.html') 

if __name__=='__main__':
    app.run(debug=True)
