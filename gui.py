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
            [sg.Column([[sg.Submit(), sg.Cancel()]], justification='center')],
            [sg.StatusBar("", size=(0, 1), key='-STATUS-')]
        ]

        # Create the window
        sg.change_look_and_feel('BluePurple')
        window = sg.Window("Trip Advisor", layout, margins=(100, 80), element_padding=(10, 10))

        # event
        while True:
            event, values = window.read()
            if event == 'Cancel' or event is None:
                print("You cancelled this request")
                break
            elif event == 'Submit':
                city, state, category = values['city'], values['state'], values['category']
                if city and state and category:
                    cls.geoapify_keys = {
                        "city": values['city'].lower(),
                        "state": values['state'].lower(),
                        "categories": cls.__geoapify_categories_keymap__[values['category']]
                    }
                    break

                else:
                    status = "Oops, missing some field(s)".upper()
                    window['-STATUS-'].update(status, text_color='red', background_color='white')

        window.close()

    @classmethod
    def get_keys(cls):
        return cls.geoapify_keys
