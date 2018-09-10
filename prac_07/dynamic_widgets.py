"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Modified from dyanmic widgets, 11/09/2018
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app.
        """
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.phonebook = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Jimbo Jumbotron", "More names", "Even more names", "Etc etc"]

    def build(self):
        """
        Build the Kivy GUI.
        """
        self.title = "Dynamic Phonebook"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        """
        for name in self.phonebook:
            temp_button = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_button)


DynamicWidgetsApp().run()