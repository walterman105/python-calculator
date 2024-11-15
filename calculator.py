import tkinter as tk
from tkinter import *

top = Tk()

top.title("Calculator")
top.geometry("180x300")
top.resizable(width=False, height=False)

answer = Entry(top, width=26)


def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get())
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.delete(0, tk.END)


b0 = Button(top, text="0", width=12, height=3, command=lambda: show("0"))
b1 = Button(top, text="1", width=5, height=3, command=lambda: show("1"))
b2 = Button(top, text="2", width=5, height=3, command=lambda: show("2"))
b3 = Button(top, text="3", width=5, height=3, command=lambda: show("3"))
b4 = Button(top, text="4", width=5, height=3, command=lambda: show("4"))
b5 = Button(top, text="5", width=5, height=3, command=lambda: show("5"))
b6 = Button(top, text="6", width=5, height=3, command=lambda: show("6"))
b7 = Button(top, text="7", width=5, height=3, command=lambda: show("7"))
b8 = Button(top, text="8", width=5, height=3, command=lambda: show("8"))
b9 = Button(top, text="9", width=5, height=3, command=lambda: show("9"))

b_multiply = Button(top, text="x", width=5, height=3, command=lambda: show("*"))
b_divide = Button(top, text="÷", width=5, height=3, command=lambda: show("/"))
b_add = Button(top, text="+", width=5, height=3, command=lambda: show("+"))
b_subtract = Button(top, text="-", width=5, height=3, command=lambda: show("-"))

b_period = Button(top, text=".", width=5, height=3, command=lambda: show("."))
b_equal = Button(top, text="=", width=5, height=7, background="orange", command=lambda: show("="))

b_delete = Button(top, text="⌫", width=5, height=3, command=lambda: answer.delete(len(answer.get())-1, tk.END))
b_clear = Button(top, text="C", width=5, height=3, command=lambda: answer.delete(0, tk.END))

answer.grid(row=0, column=0, columnspan=4)

b0.grid(row=5, column=0, columnspan=2)
b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

b_clear.grid(row=3, column=3)
b_delete.grid(row=2, column=3)

b_period.grid(row=5, column=2)
b_equal.grid(row=4, column=3, rowspan=2)

b_add.grid(row=1, column=0)
b_subtract.grid(row=1, column=1)
b_multiply.grid(row=1, column=2)
b_divide.grid(row=1, column=3)

top.mainloop()
