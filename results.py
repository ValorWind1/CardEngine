
from tkinter import Label

from PIL import Image, ImageTk

import ex
import displayCards

def showPicResults():

    image = Image.open("ImageFile.png")


    tkimage = ImageTk.PhotoImage(image)
    label1 = Label(ex.ctr_mid, image=tkimage)
    label1.image = tkimage
    label1.pack(side="left")

    image1 = Image.open("ImageFile1.png")
    tkimage1 = ImageTk.PhotoImage(image1)
    label1 = Label(ex.ctr_mid, image=tkimage1)
    label1.image = tkimage1
    label1.pack(side="right")

def showDataResults():
    displayCards.main()


    label_11 = Label(ex.ctr_mid,text="results:" , bg="SkyBlue1")
    label_11.pack(side = "bottom",padx=2,pady=2)


def main():
    showPicResults()
    showDataResults()


if __name__ == '__main__':
    main()