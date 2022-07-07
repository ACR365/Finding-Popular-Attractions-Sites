import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.geoapify.com/v1/geocode/search?city=Houston&state=Texas&format=json&apiKey=ccc449b727344041a2a3038f3eb7e098"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url, headers=headers).json()

x = resp["results"]

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





#print(resp.status_code)
#print(resp.json())
#print(y)