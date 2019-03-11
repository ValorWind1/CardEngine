import kivy
import sqlite3
import sys

db_conn = sqlite3.connect('test.db')

print("DB Created")



db_conn.close()

print("DB Closed")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

class StudentListButton(ListItemButton):
    pass
class StudentDB(BoxLayout):
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_student(self):
        # Get the students name from testInputs
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

        # Add to listview
        self.student_list.adapter.data.extend([student_name])
        # Reset the Listview
        self.student_list._trigger_reset_populate()

    def delete_student(self):
        # If a list item is selected
        if self.student_list.adapter.selection:
            #Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
            # Remove the matching item
            self.student_list.adapter.data.remove(selection)
            #Reset the ListView
            self.student_list._trigger_reset_populate()

    def replace_student(self):
        # If a list item is selected
        if self.student_list.adapter.selection:
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text
            # Remove the matching item
            self.student_list.adapter.data.remove(selection)
            # Get the students name from testInputs
            self.student_list.adapter.data.extend([student_name])
            # Add the updated data to the list
            self.student_list._trigger_reset_populate()




class StudentDBApp(App):
    def build(self):
        return StudentDB()

dbApp = StudentDBApp()
dbApp.run()