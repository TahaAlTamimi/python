#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:30:02 2019

@author: owner
"""

from flask import Flask
app=Flask(__name__)
@app.route('/<name>')
# =============================================================================
# @app.route('/ta/<name>')
# =============================================================================
def hello_world(name):
    return '<html><body>`<h1>Hello, World! <p>%s</p></h1></body></html>' %name
if __name__=='__main__':
    app.run(debug=True)
    
