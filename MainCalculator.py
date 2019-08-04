from tkinter import *
import math

class calc:
    def shub(self):
        self.newtext = self.e.get()

    def equals(self):
        self.shub()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input')
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)

    def squareroot(self):
        self.shub()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input')
        else:
            self.sqrtval = math.sqrt(self.value)
            self.e.delete(0,END)
            self.e.insert(0,self.sqrtval)

    def square(self):
        self.shub()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input')
        else:
            self.sqval = math.pow(self.value,2)
            self.e.delete(0,END)
            self.e.insert(0,self.sqval)

    def clearall(self):
        self.e.delete(0,END)

    def clear1(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0,END)
        self.e.insert(0,self.txt)

    def action(self,argi):
        self.e.insert(END,argi)

    def __init__(self,master):
        master.title('CALCULATOR')
        master.geometry("270x249+870+180")
        self.e = Entry(master)
        self.e.grid(row=0, column=0, columnspan=6,pady=3)
        self.e.focus_set()

        Button(text="=", width=10,height=3, command=lambda: self.equals()).grid(row=4, column=4, columnspan=2,sticky=NSEW)
        Button(text='AC', width=5,height=3, command=lambda: self.clearall()).grid(row=1, column=4)
        Button(text='C', width=5,height=3, command=lambda: self.clear1()).grid(row=1, column=5)
        Button(text="+", width=5,height=3, command=lambda: self.action('+')).grid(row=4, column=3)
        Button(text="x", width=5,height=3, command=lambda: self.action('*')).grid(row=2, column=3)
        Button(text="-", width=5,height=3, command=lambda: self.action('-')).grid(row=3, column=3)
        Button(text="÷", width=5,height=3, command=lambda: self.action('/')).grid(row=1, column=3)
        Button(text="%", width=5,height=3, command=lambda: self.action('%')).grid(row=4, column=2)
        Button(text="7", width=5,height=3, command=lambda: self.action(7)).grid(row=1, column=0)
        Button(text="8", width=5,height=3, command=lambda: self.action(8)).grid(row=1, column=1)
        Button(text="9", width=5,height=3, command=lambda: self.action(9)).grid(row=1, column=2)
        Button(text="4", width=5,height=3, command=lambda: self.action(4)).grid(row=2, column=0)
        Button(text="5", width=5,height=3, command=lambda: self.action(5)).grid(row=2, column=1)
        Button(text="6", width=5,height=3, command=lambda: self.action(6)).grid(row=2, column=2)
        Button(text="1", width=5,height=3, command=lambda: self.action(1)).grid(row=3, column=0)
        Button(text="2", width=5,height=3, command=lambda: self.action(2)).grid(row=3, column=1)
        Button(text="3", width=5,height=3, command=lambda: self.action(3)).grid(row=3, column=2)
        Button(text="0", width=5,height=3, command=lambda: self.action(0)).grid(row=4, column=0)
        Button(text=".", width=5,height=3, command=lambda: self.action('.')).grid(row=4, column=1)
        Button(text="(", width=5,height=3, command=lambda: self.action('(')).grid(row=2, column=4)
        Button(text=")", width=5,height=3, command=lambda: self.action(')')).grid(row=2, column=5)
        Button(text="√", width=5,height=3, command=lambda: self.squareroot()).grid(row=3, column=4)
        Button(text="x²", width=5,height=3, command=lambda: self.square()).grid(row=3, column=5)

root = Tk()
obj=calc(root)
root.mainloop()


