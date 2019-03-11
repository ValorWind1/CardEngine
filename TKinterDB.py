from tkinter import *
from tkinter import ttk
import sqlite3


class CardDB:
    # Class Fields
    db_conn = 0
    theCursor = 0
    curr_card = 0

    def setup_db(self):
        # Open or create DB
        self.db_conn = sqlite3.connect('card.db')
        # Create Cursor
        self.theCursor = self.db_conn.cursor()
        try:
            # Create the table if it doesn't exist
            self.db_conn.execute(
                "CREATE TABLE if not exists Cards(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, CName TEXT NOT NULL, LName TEXT NOT NULL); ")

            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("ERROR : Table doesn't exist")

    def card_submit(self):
        # Insert student into the DB
        self.db_conn.execute("INSERT INTO Cards(CName, LName) " +
                             "VALUES (' " +
                             self.cn_entry_value.get() + "','" +
                             self.ln_entry_value.get() + "')")

        # Clear entry boxes
        self.cn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")
        # Update list box
        self.update_listbox()

    def update_listbox(self):
        # Delete items in List Box
        self.list_box.delete(0, END)
        # Get students from the db
        try:
            result = self.theCursor.execute("SELECT ID, CName, LName FROM Cards")

            for row in result:
                card_id = row[0]
                card_cname = row[1]
                card_lname = row[2]

                # Put students in LB
                self.list_box.insert(card_id,
                                     card_cname + " " +
                                     card_lname)

        except sqlite3.OperationalError:
            print(" Table doesn't exist")
        except:
            print("1 : Couldn't retrieve data from database")

    def load_card(self, event=None):
        # Get index selected which is the student id
        lb_widget = event.widget
        index = str(lb_widget.curselection()[0] + 1)

        # Store the current student index
        self.curr_card = index
        # Retrieve student list from db
        try:
            result = self.theCursor.execute("SELECT ID, CName, LName FROM Students WHERE ID=" + index)

            for row in result:
                card_id = row[0]
                card_cname = row[1]
                card_lname = row[2]

                # Set the names in the entries
                self.cn_entry_value.set(card_cname)
                self.ln_entry_value.set(card_lname)

        except sqlite3.OperationalError:
            print(" Table doesn't exist")
        except:
            print("2 : Couldn't retrieve data from database")

    def update_card(self):
        # Update based on current student
        try:
            self.db_conn.execute("UPDATE Students SET CName ='" +
                                 self.cn_entry_value.get() +
                                 "', LName = '" +
                                 self.ln_entry_value.get() +
                                 "' WHERE ID=" +
                                 self.curr_card)
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("Database Couldn't be updated")

        self.cn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        self.update_listbox()

    def __init__(self, root):
        root.title("Card Database")
        root.geometry("300x350")

        # 1st row
        cn_label = Label(root, text="Card Name")
        cn_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.cn_entry_value = StringVar(root, value="")
        self.cn_entry = ttk.Entry(root, textvariable=self.cn_entry_value)
        self.cn_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # 2nd row
        ln_label = Label(root, text="Label")
        ln_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.ln_entry_value = StringVar(root, value="")
        self.ln_entry = ttk.Entry(root, textvariable=self.ln_entry_value)
        self.ln_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # 3rd row

        self.submit_button = ttk.Button(root, text="Submit", command=lambda: self.card_submit())

        self.submit_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.update_button = ttk.Button(root, text="Update", command=lambda: self.update_card())

        self.update_button.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # 4th row

        scrollbar = Scrollbar(root)
        self.list_box = Listbox(root)
        self.list_box.bind('<<ListboxSelect>>', self.load_card)

        self.list_box.insert(1, "Cards Here")

        self.list_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=W + E)

        self.setup_db()

        self.update_listbox()


root = Tk()

cardDB = CardDB(root)

root.mainloop()
