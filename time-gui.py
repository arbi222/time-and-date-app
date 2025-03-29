from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock ")
root.resizable(width = False, height = False)
root.configure(background = "black")
root.iconbitmap(r'clock.ico')
root.geometry('1480x470+0+0')

def time():
	string = strftime('%H : %M : %S %p')
	label.config(text = string)
	label.after(1000, time)

def calendar():
	string1 = strftime('%a / %m / %Y ')
	label1.config(text = string1)



label = Label(root, font=('times-new-roman', 160 ) , background = 'black' , foreground = 'red')
label.pack(anchor = 'center')
time()

label1 = Label(root, font=('times-new-roman', 166 ) , background = 'black' , foreground = 'cyan')
label1.pack(anchor = 'center')
calendar()

mainloop()	
