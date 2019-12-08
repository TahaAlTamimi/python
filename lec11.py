#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:34:21 2019

@author: owner
"""
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.colorchooser import * 

# =============================================================================
# par=Tk()
# val1=StringVar()
# val2=StringVar()
# name=Label(par,text='name').grid(row=0,column=0)
# e1=Entry(par,textvariable=val1).grid(row=0,column=1)
# 
# password=Label(par,text='password').grid(row=1,column=0)
# 
# e2=Entry(par,textvariable=val2).grid(row=1,column=1)
# 
# 
# def act():
#     if val1.get()=='orange' and val2.get()=='codingacademy':
#        z= messagebox.showinfo('proof','successful login')
#        if z=="ok":
#             par.destroy()
#     else:
#         messagebox.showinfo('error','password error or name error')
# sumbit=Button(par,text='sumbit',command=act).grid(row=4,column=0)
# 
# 
# 
# par.mainloop()
# =============================================================================


win=Tk()
screen_width=win.winfo_screenwidth()
screen_height=win.winfo_screenheight()
w="500x500+"+str(int((screen_width-500)/2))+"+"+str(int((screen_height-500)/2))
win.geometry(w)
txt=scrolledtext.ScrolledText(win,width=40,height=10)

def act():
    messagebox.showinfo('hello','This is a message')
    
def acte():
    par=Tk()
    val1=StringVar()
    val2=StringVar()
    name=Label(par,text='name').grid(row=0,column=0)
    e1=Entry(par,textvariable=val1).grid(row=0,column=1)

    password=Label(par,text='password').grid(row=1,column=0)

    e2=Entry(par,textvariable=val2).grid(row=1,column=1)


    def act():
            if val1.get()=='orange' and val2.get()=='codingacademy':
                z= messagebox.showinfo('proof','successful login')
                if z=="ok":
                    par.destroy()
            else:
                messagebox.showinfo('error','password error or name error')
    sumbit=Button(par,text='sumbit',command=act).grid(row=4,column=0)



    par.mainloop()
    
def acted():
    win=Tk()
    screen_width=win.winfo_screenwidth()
    screen_height=win.winfo_screenheight()
    w="500x500+"+str(int((screen_width-500)/2))+"+"+str(int((screen_height-500)/2))
    win.geometry(w)
    txt=scrolledtext.ScrolledText(win,width=40,height=10,wrap=WORD)
    txt.grid(column=0,row=1)
    for i in range(20):
        txt.insert(END, "The count is "+ str(i) + "\n")
#Pushes the scrollbar and focus of text to the end of the text input.
        txt.yview(END)
        txt.pack()
    win.mainloop() 
    
    

a=Button(win,text='open message',command=act)
b=Button(win,text='open child windows 1',command=acte)
c=Button(win,text='open child windows 2',command=acted)
a.pack()
b.pack()
c.pack()
win.mainloop()


# =============================================================================




#Q3 =============================================================================
# root = Tk()
# def getcolor():
#     color=askcolor()
#     root.config(background=color[1])
# 
# Button(root,text="select",command=getcolor).pack()
# mainloop()
# =============================================================================



# =============================================================================


# =============================================================================
# from tkinter import *
# from tkinter import messagebox
# from tkinter import scrolledtext
# def open_child1():
#     dialog_title=""
#     dialog_text="This is a message"
#     answer=messagebox.showinfo(dialog_title,dialog_text)
# def open_child2():
#     top=Tk()
#     top.title('Child window 2')
#     top.geometry('400x250')
#     name=Label(top,text="Emy Number").place(x=30,y=50)
#     email=Label(top,text="Emy Name").place(x=30,y=90)
#     e1=Entry(top).place(x=100,y=50)
#     e2=Entry(top).place(x=100,y=90)
#     button=Button(top,text="Quit",command=top.destroy).place(x=150,y=150)
#     button.pack()
#     top.mainloop()
# def open_child3():
#     win=Tk()
#     win.title("Welcome")
#     win.geometry('350x200')
#     txt=scrolledtext.ScrolledText(win,width=40,height=10)
#     txt.grid(column=0,row=0)
#
#
#
# root = Tk()
# root.title('Root window')
# Button(root, text = 'open child window 1', command = open_child1).grid()
# Button(root, text = 'open child window 2', command = open_child2).grid()
# Button(root, text = 'open child window 3', command = open_child3).grid()
# root.mainloop()
#
# =============================================================================


































# =============================================================================
# root= Tk()
# =============================================================================
# =============================================================================
# root= Tk(className="my first GUI")
# 
# screen_width=root.winfo_screenwidth()
# screen_height=root.winfo_screenheight()
# w="500x500+"+str(int((screen_width-500)/2))+"+"+str(int((screen_height-500)/2))
# root.geometry(w)
# label=Label(root,text="Hello world",padx=10,pady=10)
# label.pack()
# def Pressed():
#      dialog_title="please answer"
#      dialog_text="Do you like to travel?"
#      answer=messagebox.askquestion(dialog_title,dialog_text)
#      if answer=='yes':
#         print("I like this !")
#      else:
#         print("You must have clicked the wrong button by accident.")
#     
# b=Button(root,text="sample",fg="red",command=Pressed)
# b.pack()
# root.mainloop()
# print("screen_width:",screen_width)
# print("screen_height=",screen_height)
# =============================================================================
# =============================================================================
# win=Tk()
# screen_width=win.winfo_screenwidth()
# screen_height=win.winfo_screenheight()
# w="500x500+"+str(int((screen_width-500)/2))+"+"+str(int((screen_height-500)/2))
# win.geometry(w)
# txt=scrolledtext.ScrolledText(win,width=40,height=10)
# 
# v=StringVar() 
# e=Entry(win,textvariable=v)
# e.pack()
# def act():
#     print('you entered')
#     print('%s' %v.get())
# b=Button(win,text='press',command=act)
# b.pack()
# win.mainloop()
# =============================================================================
# =============================================================================
# root=Tk()
# root.title('tamam')
# 
# def notdone():
#     messagebox.showinfo('not implement','not not') 
# 
# top=Menu(root)
# root.config(menu=top)
# 
# file=Menu(top,tearoff=0)
# file.add_command(label='new',command=notdone)
# file.add_command(label='open',command=notdone)
# file.add_separator()
# file.add_command(label='Quit',command=root.destroy)
# 
# top.add_cascade(label='File',menu=file)
# 
# edit=Menu(top,tearoff=0)
# edit.add_command(label='cut',command=notdone)
# edit.add_command(label='paste',command=notdone)
# top.add_cascade(label='edit',menu=edit)
# 
# root.mainloop()
# =============================================================================
# =============================================================================
# def getcolor():
#     color=askcolor()
#     print(color)
# 
# Button(text='select color',command=getcolor).pack()
# mainloop()
# 
# =============================================================================









