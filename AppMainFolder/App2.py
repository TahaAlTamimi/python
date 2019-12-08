#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:49:04 2019

@author: owner
"""

from flask import Flask ,render_template
app=Flask(__name__)
@app.route('/score/<int:score>')
# =============================================================================
# @app.route('/ta/<name>')
# =============================================================================
def index(score):
    return render_template('Index4.html',marks=score) 

if __name__=='__main__':
    app.run(debug=True)