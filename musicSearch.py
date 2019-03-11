from tkinter import filedialog
from tkinter import *


a = Tk()



def musicFile():
    global file
    file = filedialog.askopenfile()
    label = Label(text=file).pack()
    print(file)


button = Button(text="open file", width=30, command=musicFile).pack()
if button:
    print(musicFile.name)



a.mainloop()