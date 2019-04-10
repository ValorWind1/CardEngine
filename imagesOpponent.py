import tkinter.messagebox
from tkinter import Label, Button, Menu, Tk
from tkinter import filedialog
from PIL import Image, ImageTk

import ex

#root = Tk()

#menubar = Menu(root)
#root.config(menu=menubar)

#submenu = Menu(menubar, tearoff=0)


# create the sub M
def browse_fileIM1():
    global picturefile1
    picturefile1 = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])


#menubar.add_cascade(label="File", menu=submenu)
#submenu.add_command(label="Open", command=browse_fileIM1)
#submenu.add_command(label="Exit", command=root.destroy)

#root.geometry("800x600")
#root.title("Picture")

#text = Label(root, text="Choose your picture")
#text.pack()


def playI1():
    try:

        global new_img1
        global label2
        im = Image.open(picturefile1)
        new_img1 = im.resize((150, 250))
        new_img1.save("ImageFile1.png", "JPEG", optimize=True)
        tkimage = ImageTk.PhotoImage(new_img1)
        label2 = Label(ex.ctr_mid, image=tkimage)
        label2.image = tkimage
        label2.pack(side="right", padx=2, pady=5)




    except:
        tkinter.messagebox.showerror(" You have not selected a File", "You have not selected a File, Try again")
        print("Error")


def stopIM1():
    label2.destroy()


#play = Button(root, text="Open Image", width=30, command=playI1)
#play.pack()

#stop = Button(root, text="Close Image", width=30, command=stopIM1)
#stop.pack()

#root.mainloop()