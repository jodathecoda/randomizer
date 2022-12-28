import os
from inspect import stack
from pickletools import stackslice
from tkinter import *
from math import sqrt
import random
import subprocess

global cwd
cwd = os.getcwd()

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

win = Tk() # This is to create a basic window
win.geometry("100x100")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")
win.iconbitmap("Randomizer.ico")


def randomizer():
   #rnd = random.uniform(1.0,99.9)
    rnd = random.randint(1,100)
    input_text.set(str(rnd)[0:5] + "%")
expression = ""
input_text = StringVar()
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()
turn_ggop = Button(btns_frame, text = "RAND", fg = "black", width = 15, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: randomizer()).grid(row = 5, column = 2, columnspan = 2, padx = 1, pady = 1)
#turn_ggop = Button(btns_frame,text = "RR", width = 15, height = 3,command = lambda: randomizer()).grid(row = 5, column = 2, columnspan = 2, padx = 1, pady = 1)
win.mainloop()
