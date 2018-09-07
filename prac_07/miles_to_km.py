"""
App to convert miles to km
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKmApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Miles to km"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_increment(self, value):
        """ handle increment buttons that add or minus 1 from th text input """

        try:
            self.root.ids.miles_input.text = str(float(self.root.ids.miles_input.text) + value)
        except ValueError:
            self.root.ids.miles_input.text = str(value)

    def handle_conversion(self, miles):
        """ handle the conversion"""
        # try:
        #     self.root.ids.output_label.text = "{:.3f}".format(miles * 1.609344)
        # except ValueError:
        #     self.root.ids.output_label.text = "0.0"

        try:
            self.root.ids.output_label.text = "{:.3f}".format(float(miles)*1.609344)
        except ValueError:
            self.root.ids.output_label.text = "0.0"
        except TypeError:
            self.root.ids.output_label.text = "0.0"
        except ValueError:
            self.root.ids.output_label.text = "0.0"


MilesToKmApp().run()
