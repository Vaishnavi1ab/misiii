import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


def musicWindow():

    print("\n\t\t\t\tIP MESSENGER")

   
    window=Tk()
    window.title('Music Window')
    window.geometry('300x300')
    window.configure(bg='lightSkyBlue')





    selectLabel = Label(window, text= "Select song",bg='LightSkyBlue', font = ("Calibri",10))
    selectLabel.place(x=2, y=1)

    listbox = Listbox(window,height = 19,width = 39,activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play",bd=1,width=10,bg='SkyBlue', font = ("Calibri",10))
    playButton.place(x=30,y=200)

   
    stop=Button(window,text="Stop",bd=1,width=10,bg='SkyBlue', font = ("Calibri",10))
    stop.place(x=200,y=200)

 
    Upload=Button(window,text="Upload",bd=1,width=10,bg='SkyBlue', font = ("Calibri",10))
    Upload.place(x=30,y=250)

    Download = Label(window, text= "Chat Window", font = ("Calibri",10))
    Download.place(x=200, y=250)


    infolabel = Label(window, text= "",fg= "blue", font = ("Calibri",8))
    infolabel.place(x=4, y=280)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
   
setup()

