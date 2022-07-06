import requests
import json
from requests.structures import CaseInsensitiveDict





















#Main Function
GEOAPIFY_APIKEY = 'ccc449b727344041a2a3038f3eb7e098'


city_prompt = "Enter the city of where you want to find the attractions of: "
city = str(raw_input(city_prompt))
state_prompt = "Enter the city's full state name: "

if len(state_prompt) == 2:
    while len(state_prompt) == 2:
        state_prompt = str(input("Error: You entered the initals of the state. Please enter the full name of the state: "))

state = str(raw_input(state_prompt))


geocoding_url = "https://api.geoapify.com/v1/geocode/search?city=" + city + "&state=" + state + "&format=json&apiKey=" = GEOAPIFY_APIKEY
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(geocoding_url, headers=headers).json()
print(resp)

"""
lon = ""
lat = ""

i = 0
while i != len(x):
    coord_finder = x[i]

    for j in coord_finder:
        if j == 'lon' or j == 'lat':
            if j == 'lon':
                lon = coord_finder[j]
                print(lon)
            elif j == 'lat':
                lat = coord_finder[j]
                print(lat)

    if lon == "" and lat == "":
        i += 1
    else:
        break

radius = "5000"
places_url = "https://api.geoapify.com/v2/places?categories=tourism&filter=circle:{lon},{lat},{radius}&&apiKey={GEOAPIFY_APIKEY}" 

categories_prompt = "Enter the name of the category of the attraction you want to find\n[1]Accomodation [2]Ac"
location_data = requests.get(places_url).json()

print(location_data)
"""

"""
i = 0
location_values = location_data.values()
while i != len(location_values):
    print(l)
"""

    
