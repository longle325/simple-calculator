import tkinter as tk
from math import *
import tkinter.messagebox #N3
from tkinter.constants import SUNKEN

window=tk.Tk()
window.title('Calculator')
window.geometry('480x560')
frame=tk.Frame(master=window,bg="white",padx=0,pady=0)
frame.pack()#N3
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=5, width=23, font=("Times New Roman", 25))
entry.grid(row=0, column=0, columnspan=4, pady=10)

def myclick(number):
	entry.insert(tk.END, number)


def equal(event=None):
    try:
        y = str(entry.get())
        y = y.replace('𝝅','pi')
        y = y.replace('x','*')
        r = str(eval(y))
        entry.delete(0, tk.END)
        entry.insert(0, r)
    except:
        tkinter.messagebox.showinfo("Error","Syntax Error")


def clear():
	entry.delete(0, tk.END)
buttons = ['(',')','Del','sin','cos','tan','𝝅','7','8','9','/','4','5','6','x','1','2','3','-','0','.','+','=']
m = 1
n = 0
content = [' '] * len(buttons)
for i in range(len(buttons)) :
    if len(buttons[i]) == 1 :
        if buttons[i] == '=' :
            content[i] = tk.Button(master=frame, text= buttons[i], padx=40, pady=20, command=equal)
            content[i].grid(row=m, column=n,pady = 2,padx = 2)
            window.bind('<Return>', equal)  
            window.bind('=',equal)
        else :
            content[i] = tk.Button(master=frame, text= buttons[i], padx=40, pady=20, command= lambda i=i: myclick(buttons[i]))
            content[i].grid(row=m, column=n,pady = 2,padx = 2)
    elif buttons[i] == 'Del' :
        content[i] = tk.Button(master=frame, text= buttons[i], padx=56, pady=20, command=clear)
        content[i].grid(row=m, column=n,pady=2,columnspan = 2)
        m+=1
        n=0
        continue
    else :
        content[i] = tk.Button(master=frame, text= buttons[i], padx=35, pady=20, command= lambda i=i: myclick(buttons[i]))
        content[i].grid(row=m, column=n,pady=3,padx=2)
    n+=1
    if n > 3 :
        m+=1
        n = 0
window.mainloop()
