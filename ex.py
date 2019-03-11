from tkinter import *
#import os





root = Tk()
root.title('Card Game engine')
root.geometry('{}x{}'.format(1000,600))

# Main  frames
top_frame = Frame(root, bg='red3', width=650, height=700, pady=10)
center = Frame(root, bg='black', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='snow', width=450, height=45, pady=3)
btm_frame2 = Frame(root, bg='red3', width=450, height=60, pady=3)
label_1 = Label(root, text = " Jose Acevedo , Daniel Leyghton",bg ="snow")
c = Checkbutton(root, text=" Create Card size")


# boxes main Layout
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")
label_1.grid(row=4, sticky=E)


# Top frame Widgets
model_label = Label(top_frame,text='Card Maker',bg="snow")
width_label = Label(top_frame, text='Width:')
length_label = Label(top_frame, text='Length:')
entry_W = Entry(top_frame, background="snow")
entry_L = Entry(top_frame, background="snow")

# Top Frame widgets Layout
model_label.grid(row=0, columnspan=3,sticky=W,pady = 5)
width_label.grid(row=2, column=0)
length_label.grid(row=2, column=5)
entry_W.grid(row=2, column=1)
entry_L.grid(row=2, column=6)
c.grid(row=0,sticky="se",pady = "10")
label_2= Label(root, text = "Card Preview",bg ="snow")

# Center Widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='snow', width=300, height=190, padx=50, pady=50)
ctr_mid = Frame(center, bg='linen', width=300, height=190, padx=50, pady=50)
ctr_right = Frame(center, bg='snow', width=300, height=190, padx=50, pady=50)

label_2.grid(row=1, sticky="n",pady = "10")
ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")


# test area
#def testArea():


    # this is where we call the main function that was defined in the other program






# Mouse event if you click center-right most widget
def leftClick(event):
    print(" OK")
ctr_left.bind("<Button-1>",leftClick)


# This is the exit/save options toolbar at the very top
def doNothing():
    print("...")
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label=" New",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu = editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# Insert Image/print buttons / right side

insertButton = Button(ctr_right,text="Insert picture", command =doNothing)
insertButton.pack(side=TOP,padx=2,pady=5)
printButton = Button(ctr_right,text="Insert music", command =doNothing)
printButton.pack(side=TOP,padx=2,pady=5)



# second row of right buttons

insertButton = Button(ctr_right,text="Deck", command =doNothing)
insertButton.pack(side=TOP,padx=2,pady=5)
printButton = Button(ctr_right,text="Multiply", command =doNothing)
printButton.pack(side=TOP,padx=2,pady=5)

ctr_right.grid(row=0, column=2, sticky="ns")

# Insert buttons / left side

insertButton1 = Button(ctr_left,text="Game Rules", command =doNothing)
insertButton1.pack(side=TOP,padx=2,pady=5)
printButton1 = Button(ctr_left,text=" Card Labels", command =doNothing()).pack()
insertButton1.pack(side=TOP,padx=2,pady=5)
#os.system("TKinterDB.py")
# insertbutton 1 at the top 2 lines


#2nd row of buttons

insertButton2 = Button(ctr_left,text="Music", command =doNothing)
insertButton2.pack(side=TOP,padx=2,pady=5)
printButton2 = Button(ctr_left,text="effects", command =doNothing)
printButton2.pack(side=TOP,padx=2,pady=5)

ctr_left.grid(row=0, column=0, sticky="ns")


# photos !!

photo = PhotoImage(file="p5.gif")
labelp = Label(root,image=photo)
labelp.grid(row=0,sticky="s",pady = "2")

# bottom pic

photo1 = PhotoImage(file="p1.gif")
labelp1 = Label(btm_frame2,image=photo1)
labelp1.grid(row=0,padx=5,pady = 5)

# TKINTER DB PROGRAM



#mbutton = Button(text = "Let's Go", command= openProgram).pack()


root.mainloop()