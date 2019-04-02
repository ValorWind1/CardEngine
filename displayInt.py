import re
from tkinter import messagebox

def displayint():
    file = open('output.txt', 'r')

    file = file.read()

    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)

    print(numbers)

    messagebox.showinfo("Numbers entered", numbers)
def main():
    displayint()
if __name__ == '__main__':
    main()