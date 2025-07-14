import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import pyttsx3
from tkinter import filedialog
import os

root = Tk()
root.title("Text to Speech")
root.geometry("900x460")
root.resizable(False, False)
root.configure(bg="#FF7F50")

engine=pyttsx3.init()

def speaknow() :
    text=text_area.get(1.0, END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice() :
        if(gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else :
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

def download() :
    text=text_area.get(1.0, END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice() :
        if(gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else :
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

# Icon
icon_image = Image.open("TTS-Python-Tkinter/vecteezy_3d-megaphone-illustration_11048550.png")
icon_photo = ImageTk.PhotoImage(icon_image.resize((32, 32)))
root.iconphoto(False, icon_photo)

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=105)
Top_frame.place(x=0, y=0)
Label(Top_frame,text="TEXT TO SPEECH - TTS",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)
# Logo
logo_image = Image.open("TTS-Python-Tkinter/vecteezy_gold-microphone-broadcast-or-karaoke-3d-render-element_9335954.png")
logo_photo = ImageTk.PhotoImage(logo_image.resize((80, 80)))
logo_label = Label(Top_frame, image=logo_photo, bg="white")
logo_label.image = logo_photo
logo_label.place(x=10, y=10)

###############
text_area=Text(root,font="Robote 20",bg="#E3C371",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=145,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)
      
gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14 ",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','slow'],font="arial 14 ",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set("Normal")

btn=Button(root,text="speak",width=11,font='arial 12 bold',command=speaknow)
btn.place(x=550,y=280)

save=Button(root,text="save",width=11,font='arial 12 bold',command=download)
save.place(x=730,y=280)

root.mainloop()
