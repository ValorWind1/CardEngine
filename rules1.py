from  tkinter import *



def rules1():
    print
    "New File!"


def rules2():
    pass

def rules3():
    pass

def About():
    print
    "This is a simple example of a menu"


root = Tk()
menu = Menu(root)
root.config(menu=menu)
rulemenu = Menu(menu)
menu.add_cascade(label="File", menu=rulemenu)
rulemenu.add_command(label="Rule 1", command=rules1)
rulemenu.add_command(label="Rule 2 ", command=rules2)
rulemenu.add_command(label="Rule 3 ", command=rules3)
rulemenu.add_separator()
rulemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help About Rules ...", command=About)

mainloop()