import tast
import Images
import loadData
import ugotMail
import dateCalendar
import displayCards
import myWeb
import results
import imagesOpponent
import displayInt
import displaying_txtData
from tkinter import*
import animation



root = Tk()
root.title('Card Game engine')
root.geometry('{}x{}'.format(1000,647))

# Main  frames
top_frame = Frame(root, bg='red3', width=650, height=700, pady=10)
center = Frame(root, bg='black', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='snow', width=450, height=45, pady=3)
btm_frame2 = Frame(root, bg='red3', width=450, height=60, pady=3)
label_1 = Label(root, text = " Jose Acevedo , Daniel Leyghton",bg ="azure")
#c = Checkbutton(root, text=" Create Card size")


# boxes main Layout
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")
label_1.grid(row=4, padx="5",pady="10",sticky=E)


# Top frame Widgets
model_label = Label(top_frame,text='Card Maker',bg="snow")
width_label = Label(top_frame, text='Width:')
length_label = Label(top_frame, text='Length:')
entry_W = Label(top_frame,text = " 130 ", background="azure")
entry_L = Label(top_frame,text = " 200 ", background="azure")

# Top Frame widgets Layout
model_label.grid(row=0, columnspan=3,sticky=W,pady = 5)
width_label.grid(row=2, column=0)
length_label.grid(row=2, column=5)
entry_W.grid(row=2, column=1)
entry_L.grid(row=2, column=6)
#c.grid(row=0,sticky="se",pady = "10")
label_2= Label(root, text = "Card Preview",bg ="snow")

# Center Widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='snow', width=500, height=250, padx=5, pady=5)
ctr_mid = Frame(center, bg='alice blue', width=500, height=250, padx=5, pady=5)
ctr_right = Frame(center, bg='snow', width=500, height=250, padx=5, pady=5)

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
""""
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

insertButton = Button(ctr_right,text="Something x here ?", command =doNothing)
insertButton.pack(side=TOP,padx=2,pady=5)
#printButton = Button(ctr_right,text="Insert music", command =doNothing)
#printButton.pack(side=TOP,padx=2,pady=5)
"""
# ---------------------------------------Module Rules ----------------------------------------------------
def rule1():
    pass

def rule2():
    pass

def rule3():
    pass

def About():
    pass

menu = Menu(root)
root.config(menu=menu)
rulemenu = Menu(menu)
menu.add_cascade(label="File", menu=rulemenu)
rulemenu.add_command(label="Rule 1", command=rule1)
rulemenu.add_command(label="Rule 2 ", command=rule2)
rulemenu.add_command(label="Rule 3 ", command=rule3)
rulemenu.add_separator()
rulemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help About Rules ...", command=About)




#--------------------------------------end of rules module ------------------------------------------------

# ---------------------------------------- MODULE MUSIC !!!!-----------------------------------------------

def browseMF():
    tast.browse_file()

printButton = Button(ctr_right, text="Browse Music File", command=browseMF,bg="IndianRed1",height = 1 ,width =18)
printButton.pack(side=TOP, padx=2, pady=5)

def playM():
    tast.playM()
insertButton = Button(ctr_right,text="Play Music", command =playM,bg="IndianRed1",height = 1 ,width =18)
insertButton.pack(side=TOP,padx=2,pady=5)

def stopM():
    tast.stopM()

printButton = Button(ctr_right,text="Stop Music", command =stopM,bg="IndianRed1",height = 1 ,width =18)
printButton.pack(side=TOP,padx=2,pady=5)

ctr_right.grid(row=0, column=2, sticky="ns")

# --------------------------------- end of Module Music ----------------------------------------------------------

# --------------------------------- Picture Module --------------------------------------------------------------
def browseIM():
    Images.browse_fileIM()

insertButton2 = Button(ctr_left,text=" Browse Your Card Image", command =browseIM,bg="light coral",height = 1 ,width =23)
insertButton2.pack(side=TOP,padx=2,pady=5)

def playIM():
    Images.playIM()

insertButton1 = Button(ctr_left,text="Display Your Card", command= playIM,bg="light coral",height = 1 ,width =23)
insertButton1.pack(side=TOP,padx=2,pady=5)

def stopIM():
    Images.stopIM()

printButton2 = Button(ctr_left,text="Stop Displaying Card", command =stopIM,bg="light coral",height = 1 ,width =23)
printButton2.pack(side=TOP,padx=2,pady=5)

ctr_left.grid(row=0, column=0, sticky="ns")

def BrowseIMO():
    imagesOpponent.browse_fileIM1()

insertButton8 = Button(ctr_left,text=" Browse Opponent Card Image", command = BrowseIMO, bg= "dark turquoise",height = 1 ,width =23)
insertButton8.pack(side=TOP,padx=2,pady=5)


def playIMO():
    imagesOpponent.playI1()

printButton9 = Button(ctr_left,text="Display Opponent Card", command = playIMO, bg= "dark turquoise",height = 1 ,width =23)
printButton9.pack(side=TOP,padx=2,pady=5)

ctr_left.grid(row=0, column=0, sticky="ns")

def stopOp():
    imagesOpponent.stopIM1()

printButton13 = Button(ctr_left,text="Stop displaying opponen card", command = stopOp, bg= "dark turquoise",height = 1 ,width =23)
printButton13.pack(side=TOP,padx=2,pady=5)

# ---------------------------------- end of picture Module --------------------------------------------------------

#----------------------------------- Creating an Object , and Loading Object -------------------------------------

def openProgram():
    loadData.main()
printButton3 = Button(ctr_left,text=" Create cards", command =openProgram,height = 1 ,width =23)
printButton3.pack(side=TOP,padx=2,pady=5)

#def saveData():
    #Inputs.saveData()

#printButton4 = Button(ctr_left,text=" Save Inputs ", command =userInputs)
#printButton4.pack(side=TOP,padx=2,pady=5)

#def loadData():
    #Inputs.loadData()

#printButton5 = Button(ctr_left,text=" Load the data of your card   ", command =userInputs)
#printButton5.pack(side=TOP,padx=2,pady=5)

#def StoredData():
    #Inputs.usResult()

#printButton5 = Button(ctr_left,text=" Current Cards on our system  ", command =userInputs)
#printButton5.pack(side=TOP,padx=2,pady=5)


#----------------------------------end of creating/loading object--------------------------------------------------

#-----------------------------------Email program
def openEmail():
    ugotMail.main()

c = Checkbutton(root, text=" Create Email",command = openEmail)
c.grid(row=0,sticky="se",padx = 5, pady = "10")
#printButton4 = Button(ctr_left,text=" Save Inputs ", command =openEmail)
#printButton4.pack(side=TOP,padx=2,pady=5)

# ---------------------------------Calendar/Timer
def datetime():
    dateCalendar.dateTime()

g = Checkbutton(root, text=" Current Time/ Calendar",command = datetime)
g.grid(row=4,sticky="sw",padx= "5",pady = "20")

# --------------------------------- Print Cards / Math

def printcards():
    displayCards.openCards()

printButton4 = Button(ctr_right,text=" All cards info.", command =printcards ,height = 1 ,width =18)
printButton4.pack(side=TOP,padx=2,pady=5)

def mathCards():
    displayCards.main()

printButton5 = Button(ctr_right,text="Card vs Card", command =mathCards,height = 1 ,width =18)
printButton5.pack(side=TOP,padx=2,pady=5)

#---------------------------------- Web Module

def openingWebsite():
    myWeb.main()

printButton6 = Button(ctr_left,text=" Card Website", command =openingWebsite,bg="gold",height = 1 ,width =23)
printButton6.pack(side=TOP,padx=2,pady=5,)
#2nd row of buttons

#------------------------------- result display
def dispayingResults():
    results.showPicResults()

printButton7 = Button(ctr_right,text="Display Cards entered", command =dispayingResults,bg="light sky blue",height = 1 ,width =18)
printButton7.pack(side=TOP,padx=2,pady=5)

#------------------------------ display int
def displayint():
    displayInt.displayint()

printButton10 = Button(ctr_right,text="Display integers entered ", command =displayint,bg="light sky blue",height = 1 ,width =18)
printButton10.pack(side=TOP,padx=2,pady=5)

# ------------------------------ display int to gui
def displayguiint():
    displaying_txtData.displaynumbersGui()

printButton11 = Button(ctr_left,text="Visually see values  ", command =displayguiint,bg="dodgerblue",height = 1 ,width =23)
printButton11.pack(side=TOP,padx=2,pady=5)

# ----------------------------- multiplier

def multipleCard():
    animation.main()



printButton12 = Button(ctr_right,text="animate card", command =multipleCard,bg="light sky blue",height = 1 ,width =18)
printButton12.pack(side=TOP,padx=2,pady=5)

# ------------------------------ extra
def multipleCard():
    pass
printButton12 = Button(ctr_right,text="Extra", command =multipleCard)
printButton12.pack(side=TOP,padx=2,pady=5)
# -------------------------------------------------------- photos


photo2 = PhotoImage(file="1949852.png")
labelp2 = Label(root,image=photo2,bg="red3")
labelp2.grid(row=4,sticky="s",pady = "2")

# bottom pic

photo1 = PhotoImage(file="13-watercolor-bird-silhouette-small.png")
labelp1 = Label(root,image=photo1,bg="red3")
labelp1.grid(row=0,sticky="s",padx= 5 ,pady = 5)

photo3 = PhotoImage(file ="rcLo6KGpi.png")
labelp3 = Label(ctr_right,image=photo3,bg="snow")
labelp3.pack(side= RIGHT,padx=0,pady=0)


photo4 = PhotoImage(file ="rcLo6KGpileft.png")
labelp4 = Label(ctr_left,image=photo4,bg="snow")
labelp4.pack(side= LEFT,padx=0,pady=0)

#photo5 = PhotoImage(file ="car-with-wings-clipart-10 small.png")
#labelp5 = Label(btm_frame ,image=photo5,bg="snow")
#labelp5.pack(side= LEFT,padx=0,pady=0)

photo6 = PhotoImage(file ="vs-pn_small.png")
labelp6 = Label(ctr_mid,image=photo6,bg="alice blue")
labelp6.pack(side= BOTTOM,padx=0,pady=0)




def main ():

    root.mainloop()



if __name__ == '__main__':


    main()
