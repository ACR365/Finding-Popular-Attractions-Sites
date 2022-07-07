"""GUI setup class for travel advisor"""
import PySimpleGUI as sg


class GUI:
    __categories__ = ["hotels", "restaurants", "attraction-sites",
                      "museums", "leisure-parks", "heritage"]
    __geoapify_categories_keymap__ = {
        "hotels": "accommodation.hotel",
        "restaurants": "catering",
        "attraction-sites": "tourism",
        "museums": "entertainment.museum",
        "leisure-parks": "leisure.park",
        "heritage": "heritage",
        "": ""
    }
    geoapify_keys = {}

    @classmethod
    def setup(cls):
        layout = [
            [sg.Column([[sg.Image("back.png", size=(250, 200))]], justification='center')],
            [sg.Text('Please enter the city, state, and category of destination you are looking for :)',
                     font=("Lucida", 11))],
            [sg.Text('City', size=(15, 1), font=("Lucida", 11)), sg.InputText(key='city')],
            [sg.Text('State (in full)', size=(15, 1), font=("Lucida", 11)), sg.InputText(key='state')],
            [sg.Text('Category', size=(15, 1), font=("Lucida", 11)),
             sg.Combo(cls.__categories__, font=("Lucida", 11), key='category')],
            [sg.Column([[sg.Submit(), sg.Cancel()]], justification='center')]
        ]

        # Create the window
        sg.change_look_and_feel('BluePurple')
        window = sg.Window("Trip Advisor", layout, margins=(100, 80), element_padding=(10,10))

        # event
        event, values = window.read()

        try:
            cls.geoapify_keys = {
                "city": values['city'].lower(),
                "state": values['state'].lower(),
                "categories": cls.__geoapify_categories_keymap__[values['category']]
            }
        except Exception:
            print("Error")
        finally:
            window.close()

    @classmethod
    def get_keys(cls):
        return cls.geoapify_keys


gui = GUI()
gui.setup()
print(gui.get_keys())
