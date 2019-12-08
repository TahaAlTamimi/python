#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:42:40 2019

@author: owner
"""

from xlwt import Workbook, Formula
import xlsxwriter
import sympy as sym
# =============================================================================
# 
# x = symbols('x')
# 
# expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
# print (expr)
# print ( expr.subs(x, 7))
# 
# =============================================================================
# =============================================================================
# x,y= sym.symbols('x y')
# print( sym.expand( (x + y) ** 2 ) )
# =============================================================================
# =============================================================================
# x,y= sym.symbols('x y')
# print( sym.simplify((4*x**3 + 21*x**2 +10*x +12) )) 
# =============================================================================
# =============================================================================
# print( sym.limit(1/(x**2),x,sym.oo)) 
# =============================================================================
# =============================================================================
# print(sym.summation(2*i+i-1 ,(i,5,n)))
# =============================================================================
# =============================================================================
# print( sym.integrate(sin(x)+exp(x)*cos(x)+tan(x),x)) 
# =============================================================================
# =============================================================================
# x,y,z= sym.symbols('x y z')
# print( factor(x**3 +12*x*y*z+3*y**2*z ) ) 
# =============================================================================
# =============================================================================
# print( sym.solveset(x - 4, x))
# =============================================================================

# =============================================================================
# m1 = sym.Matrix([[5, 12, 40], [30, 70, 2]])
# m2 = sym.Matrix([2, 1, 0])
# 
# print( m1*m2 )
# =============================================================================
# =============================================================================
# from sympy.plotting import plot
# x = symbols('x')
# plot(x**3+3,(x,-10,10)) 
# =============================================================================
# =============================================================================
# from sympy import symbols
# from sympy.plotting import plot3d
# x, y = symbols('x y')
# f=x**2*y**3
# plot3d(f, (x, -6, 6), (y, -6, 6))
# =============================================================================


# =============================================================================
# workbook = xlsxwriter.Workbook('ex.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.autofilter('A1')
# data = ["This is Example",'My first export example',1,2,3]
# format = workbook.add_format()
# format.set_bold()
# format.set_font_color('red')
# format.set_font_size(20)
# worksheet.write_column('A1',data ,format)
# # =============================================================================
# # worksheet.write_comment('B1', "this is a comment")
# # =============================================================================
# # =============================================================================
# # format2 = workbook.add_format({'bold' : True, 'font_color' : 'blue'})
# # worksheet.write_column('B1' , data,format2)
# # =============================================================================
# workbook.close()
# 
# =============================================================================
#Q2 =============================================================================
# import xlsxwriter
# workbook = xlsxwriter.Workbook('example10.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.autofilter('A1:B1')
# data = ["this is example"]
# format = workbook.add_format()
# format.set_font_color('red')
# format.set_font_size(12)
# worksheet.write_column('A1:B1', data ,format)
# data2 = ["export my sheet"]
# format = workbook.add_format()
# format.set_font_color('black')
# format.set_font_size(12)
# worksheet.write_column('A2:B2', data2 ,format)
# data3=[1,2]
# data4=[3]
# for elem in data3:
#     format = workbook.add_format()
#     format.set_font_color('black')
#     format.set_font_size(12)
#     worksheet.write_column("A3:A4", data3 ,format)
# for elem in data4:
#     format = workbook.add_format()
#     format.set_font_color('red')
#     format.set_font_size(12)
#     worksheet.write_column("A5", data4 ,format)
# workbook.close()
# 
# =============================================================================

# =============================================================================
# from xlrd import open_workbook
# wb=open_workbook('tamimi.xlsx')
# for s in wb.sheets():
#     print('Sheet:',s.name)
#     for row in range(s.nrows):
#         values=[]
#         for col in range(s.ncols):
#             values.append(s.cell(row,col).value)
#         print(','.join(values))
# =============================================================================

from xlrd import open_workbook
wb = open_workbook('tamimi.xlsx')
for s in wb.sheets():
    print ("Sheet:", s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)



























# =============================================================================
# import sympy as sym
# x = sym.symbols('x')
# expr = x + 1
# print ( expr.subs(x, 2) )
# =============================================================================

# =============================================================================
# 
# import sympy as sym
# x = sym.symbols('x')
# expr= x + x**2 + 1
# print( expr.subs(x, 2) )
# =============================================================================
# =============================================================================
# import sympy as sym
# from sympy import *
# x = symbols('x')
# init_printing()
# expr= Integral(sqrt(1/x),x)
# pprint(expr)
# =============================================================================
# =============================================================================
# from sympy import *
# x = symbols('x')
# init_printing()
# expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
# pprint (expr)
# =============================================================================
# =============================================================================
# import sympy as sym
# x = sym.Symbol('x')
# y, i ,n, a, b = sym.symbols('y i n a b')
# =============================================================================
# =============================================================================
# print(  sym.expand( (x + y) ** 3 )   )
# f = x**2 + 1
# print( x)
# =============================================================================
# =============================================================================
# print( sym.simplify((x + x * y) / x))
# =============================================================================
# =============================================================================
# print(  sym.limit(sym.sin(x) / x, x, 0))
# init_printing()
# we=sym.limit(sin(x)/x,x,a)
# pprint(we)
# =============================================================================
# =============================================================================
# print(sym.integrate(exp(x)*sin(x) +
# exp(x)*cos(x), x)) 
# =============================================================================
# =============================================================================
# from sympy import symbols
# from sympy.plotting import plot
# x = symbols('x')
# plot(x**2, (x, -5, 5)) 
# 
# 
# plot((x**2, (x, -6, 6)), (x, (x, -5,5)))
# =============================================================================
# =============================================================================
# 
# from sympy import symbols
# from sympy.plotting import plot3d
# x, y = symbols('x y')
# f=x**2*y**2
# plot3d(f, (x, 5, -5), (y, 5,- 5))
# =============================================================================


# =============================================================================
# from sympy import symbols
# from sympy.plotting import plot3d
# x, y = symbols('x y')
# f=cos(x)+sin(y)
# plot3d(f, (x, -10, 10), (y, -10, 10))
# 
# =============================================================================

# =============================================================================
# from sympy import symbols, cos, sin
# from sympy.plotting import plot3d_parametric_line
# u, v = symbols('u v')
# plot3d_parametric_line(cos(u), sin(u), u, (u, -5, 5))
# =============================================================================
# =============================================================================
# from sympy import symbols, cos, sin
# from sympy.plotting import plot3d_parametric_surface
# u, v = symbols('u v')
# plot3d_parametric_surface(cos(u + v), sin(u - v), u - v, (u, -5, 5), (v, -5, 5))
# 
# =============================================================================


# =============================================================================
# from sympy import symbols
# from sympy.plotting import plot3d
# x, y = symbols('x y')
# plot3d(x*y, (x, -5, 5), (y, -5, 5))
# plot3d(x*y, -x*y, (x, -5, 5), (y, -5, 5))
# plot3d((x**2 + y**2, (x, -5, 5), (y, -5, 5)), (x*y, (x, -3, 3), (y, -3, 3)))
# 
# =============================================================================

# =============================================================================
# workbook = xlsxwriter.Workbook('example10.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.autofilter('A1:B4')
# data = ["Test",10,40,50,20]
# format = workbook.add_format()
# format.set_bold()
# format.set_font_color('red')
# format.set_font_size(20)
# worksheet.write_column('A1', data ,format)
# worksheet.write_comment('B1', "this is a comment")
# format2 = workbook.add_format({'bold' : True, 'font_color' : 'blue'})
# worksheet.write_column('B1' , data,format2)
# workbook.close()
# 
# =============================================================================

# =============================================================================
# workbook = xlsxwriter.Workbook('chart.xlsx')
# worksheet = workbook.add_worksheet()
# data = [10,40,50,20,10,50]
# worksheet.write_column('A1', data )
# 
# chart=workbook.add_chart({'type':'line'})
# chart.add_series({'values':'=Sheet1!$A$1:$A$6'})
# worksheet.insert_chart('C1',chart)
# workbook.close()
# 
# =============================================================================

# =============================================================================
# book = Workbook()
# 
# sheet1 = book.add_sheet("Sheet 1")
# sheet1.write(0,0,10)
# sheet1.write(0,1,20)
# sheet1.write(1,0,Formula('A1/B1'))
# 
# sheet2 = book.add_sheet('Sheet 2')
# row = sheet2.row(0)
# 
# row.write(0,Formula('sum(1,2,3)'))
# row.write(1,Formula('SuM(1,2,3)'))
# row.write(2,Formula("$A$1+$B$1*SUM('ShEEt 1'!$A$1:$B$2)"))
# 
# book.save('example4.xlsx')
# =============================================================================






























