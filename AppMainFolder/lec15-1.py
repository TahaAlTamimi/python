#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:53:02 2019

@author: owner
"""

# =============================================================================
# from flask import Flask ,redirect,url_for,request
# app=Flask(__name__)
# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' %name
# 
# @app.route('/login',methods=['POST','GET'])
# def login():
#     if request.method=='POST':
#         user=request.form['nm']
#         return redirect(url_for('success',name=user))
#     else:
#         user=request.args.get('nm')
#         return redirect(url_for('success',name=user))
#     
# if __name__=='__main__':
#     app.run()  
# =============================================================================
    
# =============================================================================
# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/result')
# def result():
#     dict = {
#         'phy': 50,
#         'che': 60,
#         'matchs': 70
#     }
#     return render_template('lec15-1.html', result=dict)
# 
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================
from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result',methods=['POST','GET'])

def result():
    if request.method=='POST':
        result=request.form
        return render_template('result.html',result=result)
    
    
if __name__ == '__main__':
   app.run()
   
   
   
   
   
   
   
   
   