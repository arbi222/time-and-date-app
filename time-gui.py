from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock ")
root.resizable(width = False, height = False)
root.iconbitmap(r'clock.ico')
root.geometry('920x300+0+0')
root.configure(background = "black")

def time():
	string = strftime('%H : %M : %S %p')
	label.config(text = string)
	label.after(1000, time)

def calendar():
	string1 = strftime('%a / %m / %Y ')
	label1.config(text = string1)



label = Label(root, font=('times-new-roman', 80 ) , background = 'black' , foreground = 'red')
label.pack(anchor = 'center')
time()

label1 = Label(root, font=('times-new-roman', 100 ) , background = 'black' , foreground = 'cyan')
label1.pack(anchor = 'center')
calendar()

mainloop()	
