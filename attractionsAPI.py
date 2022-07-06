GEOAPIFY_APIKEY = 'ccc449b727344041a2a3038f3eb7e098'

city_prompt = "Enter the city of where you want to find the attractions of: "
city = str(input(city_prompt))
state_prompt = "Enter the city's full state name: "

if len(state_prompt) == 2:
    while len(state_prompt) == 2:
        state_prompt = str(input("Error: You entered the initals of the state. Please enter the full name of the state: "))

state = str(input(state_prompt))
location = city + "," + state

url = "https://api.geoapify.com/v2/places?categories=tourism&filter=circle:-73.935242,40.730610,5000" + "&apiKey=ccc449b727344041a2a3038f3eb7e098" 

categories_prompt = "Enter the name of the category of the attraction you want to find\n[1]Accomodation [2]Ac"
location_data = requests.get(url).json()
print(location_data)
