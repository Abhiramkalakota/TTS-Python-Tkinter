import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk();
root.title("Text to Speech")
root.geometry("900x450")
root.resizable(False,False)
root.configure(bg="#4CF3FF")

#icon
image_icon=PhotoImage(file=r"c:\Users\koush\OneDrive\Desktop\logo.png")
root.iconphoto(False,image_icon)

#TopFrame
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file=r"c:\Users\koush\OneDrive\Desktop\logo.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)







root.mainloop();