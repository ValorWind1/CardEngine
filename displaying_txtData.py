from tkinter import *
from tkinter import Label
import ex

#root =Tk()

#root.geometry("500x500")
#root.title("results ")

def displaynumbersGui():
    file = open("output.txt")
    data = file.read()

    delimiters = ['\n', ' ', ',', '.', '?', '!', ':', 'and_what_else_you_need']
    words = data
    for delimiter in delimiters:
        new_words = []
        for word in words:
            new_words += word.split(delimiter)
        words = new_words

    file.close()
    Results = Label(ex.ctr_mid, text = new_words,bg ="dodgerblue")
    Results.pack(side="bottom",padx=0,pady=0)

#root.mainloop ()

