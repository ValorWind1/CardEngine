from tkinter import *



class TestMenu:
    def __init__(self, master):


        self.master = master
        self.menubar = Menu(self.master)

        self.casmenu = Menu(self.menubar)
        self.casmenu.wierdones = Menu(self.casmenu)
        self.casmenu.wierdones.add_command(label='A')
        self.casmenu.wierdones.add_command(label='B')
        self.casmenu.wierdones.add_command(label='C')
        self.casmenu.wierdones.add_command(label='D')

        self.casmenu.add_command(label='A')
        self.casmenu.add_command(label='B')
        self.casmenu.add_command(label='C')
        self.casmenu.add_command(label='D')
        self.casmenu.add_command(label='E')
        self.casmenu.add_command(label='F')
        self.casmenu.add_cascade(label='G',
                                         menu=self.casmenu.wierdones)

        self.casmenu.add_cascade(label='Scripts',
                                 menu=self.casmenu)

        self.unused = Menu(self.menubar)

        self.menubar.add_cascade(label="Cascade Menu", menu=self.casmenu)

        self.top = Toplevel(menu=self.menubar, width=500, relief=RAISED,
                            borderwidth=2)


def main():
    root = Tk()
    root.withdraw()
    rules = TestMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
