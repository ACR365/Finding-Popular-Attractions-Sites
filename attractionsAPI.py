import requests
import json
from requests.structures import CaseInsensitiveDict
import pprint
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
























#Main Function
gui = GUI()
gui.setup()
print(gui.get_keys())

GEOAPIFY_APIKEY = 'ccc449b727344041a2a3038f3eb7e098'

"""
geocoding_url = f"https://api.geoapify.com/v1/geocode/search?city={city}&state={state}&format=json&apiKey={GEOAPIFY_APIKEY}"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

response = requests.get(geocoding_url, headers=headers).json()
geocoding_data = response['results']

lon = ""
lat = ""

i = 0
while i != len(geocoding_data):
    coord_finder = geocoding_data[i]
    
    for j in coord_finder:
        if j == 'lon' or j == 'lat':
            if j == 'lon':
                lon = coord_finder[j]
            elif j == 'lat':
                lat = coord_finder[j]

    if lon == "" and lat == "":
        i += 1
    else:
        break

print(lon)
print(lat)

radius = "16100"
places_url = f"https://api.geoapify.com/v2/places?categories=tourism&filter=circle:{lon},{lat},{radius}&&apiKey={GEOAPIFY_APIKEY}" 

categories_prompt = "Enter the name of the category of the attraction you want to find\n[1]Accomodation [2]Ac"
location_data = requests.get(places_url).json()

pprint.pprint(location_data)



i = 0
location_values = location_data.values()
while i != len(location_values):
    print(l)
"""

    
