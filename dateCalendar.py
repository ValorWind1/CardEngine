import datetime
from tkinter import messagebox

def dateTime():
    now = datetime.datetime.now()



    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    messagebox.showinfo("The Current date and time is ", now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    dateTime()