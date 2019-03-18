import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pygame
from PIL import Image, ImageTk
import ex

root =Tk()

menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar, tearoff=0)
# create the sub M
def browse_fileIM():
    global picturefile
    picturefile = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])

    print(picturefile)
menubar.add_cascade(label="File", menu= submenu)
submenu.add_command(label="Open", command = browse_fileIM)
submenu.add_command(label="Exit", command = root.destroy)



root.geometry("800x600")
root.title("Picture")

text = Label(root , text = "Choose your picture")
text.pack()




def playIM():
    try:
        im = Image.open(picturefile)
        tkimage = ImageTk.PhotoImage(im)
        label1 = Label(ex.ctr_mid, image = tkimage)
        label1.image = tkimage
        label1.pack()


    except:
        tkinter.messagebox.showerror(" You have not selected a File","You have not selected a File, Try again")
        print("Error")

def stopIM():
    pass

play = Button(root,text="Open Image", width=30, command=playIM)
play.pack()

stop = Button(root,text="Close Image", width=30, command=stopIM)
stop.pack()


root.mainloop()