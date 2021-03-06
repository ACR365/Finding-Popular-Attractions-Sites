import requests
import json
from requests.structures import CaseInsensitiveDict
import pprint
import PySimpleGUI as sg
import gui
import sqlalchemy as db
import pandas as pd


def geocoding(gui_info, city, state, category, GEOAPIFY_APIKEY, headers):
    gui_keys = gui_info.keys()

    x = 0
    for g in gui_keys:
        if g == "city":
            city = gui_info["city"]
        elif g == "state":
            state = gui_info["state"]
        elif g == "categories":
            category = gui_info["categories"]

    geocoding_url = f"https://api.geoapify.com/v1/geocode/search?city={city}&state={state}&format=json&apiKey={GEOAPIFY_APIKEY}"
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

    radius = "16100"
    place_url = f"https://api.geoapify.com/v2/places?categories={category}&filter=circle:{lon},{lat},{radius}&&apiKey={GEOAPIFY_APIKEY}" 
    return place_url


# Main Function
GEOAPIFY_APIKEY = 'ccc449b727344041a2a3038f3eb7e098'


gui = gui.GUI()


gui.setup()
gui_info = gui.get_keys()

if gui_info == {}:
    raise Exception("Error: Missing one or more fields")

city = ""
state = ""
category = ""

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

place_url = geocoding(gui_info, city, state, category, GEOAPIFY_APIKEY, headers)
location_data = requests.get(place_url).json()

l_d = location_data["features"]

locations = []
for ld in l_d:
    location = {}
    location_check = {"name": "", "address": ""}

    location_properties = ld["properties"]

    for loc in location_properties.keys():
        if loc == "address_line1":
            value = location_properties[loc]
            location["name"] = value
        elif loc == "address_line2":
            value = location_properties[loc].replace(", United States of America","")
            location["address"] = value

    locations.append(location.copy())

df = pd.DataFrame.from_records(locations)
engine = db.create_engine('sqlite:///results_db.db')
df.to_sql('results',con = engine,if_exists = 'replace',index = False)

query = engine.execute('SELECT * FROM results;').fetchall()
gui.display_results(df)