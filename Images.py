import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pygame
from PIL import Image, ImageTk


root =Tk()

menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar, tearoff=0)
# create the sub M
def browse_file():
    global picturefile
    picturefile = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])

    print(picturefile)
menubar.add_cascade(label="File", menu= submenu)
submenu.add_command(label="Open", command = browse_file)
submenu.add_command(label="Exit", command = root.destroy)

mixer.init()

root.geometry("800x600")
root.title("Picture")

text = Label(root , text = "Choose your picture")
text.pack()

def playM():
    try:
        im = Image.open(picturefile)
        tkimage = ImageTk.PhotoImage(im)
        myvar = Label(root,image = tkimage)
        myvar.image = tkimage
        myvar.pack()

        #mixer.music.play()
    except:
        tkinter.messagebox.showerror(" You have not selected a File","You have not selected a File, Try again")
        print("Error")

def stopM():
    mixer.music.stop()

play = Button(root,text="play", width=30, command=playM)
play.pack()

stop = Button(root,text="stop", width=30, command=stopM)
stop.pack()

root.mainloop()