import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root =Tk()

menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar, tearoff=0)
# create the sub M
def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)
menubar.add_cascade(label="File", menu= submenu)
submenu.add_command(label="Open", command = browse_file)
submenu.add_command(label="Exit", command = root.destroy)

mixer.init()

root.geometry("500x500")
root.title("Music")

text = Label(root , text = "Choose your Music")
text.pack()

def playM():
    try:
        mixer.music.load(filename)
        mixer.music.play()
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