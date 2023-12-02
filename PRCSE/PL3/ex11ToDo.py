'''
The following website contains weather information for a given location (website).
a. Implement a “.py” script that uses both requests and Beautiful Soup libraries to extract
all information of this page under section “Detailed Forecast”, storing it as a “. json”
file (feel free to extract additional information that you may find relevant).
b. Implement a “.py” script that allows a given user to obtain the weather forecast for a
given day, using the information from the previously stored “. json” file.
c. As an optional exercise, parse the degrees from °F to ºC and windspeed from mph to
km/h. Additionally, make the first script (a.) configurable to fetch weather data from
other locations. Similarly, adjust the second script (b.) so that users can query for
weather data of all the supported locations.
'''
import requests
from bs4 import BeautifulSoup
import json

import requests
from bs4 import BeautifulSoup
import json

def fetch_weather_data(location_url):
    response = requests.get(location_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract information under the "Detailed Forecast" section
    detailed_forecast = soup.find(id='detailed-forecast')
    #Get times list
    forecast_row = detailed_forecast.find_all("div", {"class": "row row-odd row-forecast"})
    forecast_dictionary = {}
    for row in forecast_row: 
        forecast_label = row.find("div", {"class": "col-sm-2 forecast-label"})
        forecast_text = row.find("div", {"class": "col-sm-10 forecast-text"})
        forecast_dictionary[forecast_label.get_text(strip=True)] = forecast_text.get_text(strip=True)
    print('Dic: ', forecast_dictionary)
    # Get whether for the times


    return forecast_dictionary

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

def get_value_from_json(json_file_path, key):
    try:
        # Read the JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        # Check if the key exists in the dictionary
        if key in data:
            return data[key]
        else:
            print(f"The key '{key}' does not exist in the JSON file.")
            return None

    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return None

def get_weather_forecast(json_file, day):
    with open(json_file, 'r') as json_file:
        data = json.load(json_file)

    # Retrieve the weather forecast for the given day
    forecast_key = f'forecast_{day}'
    
    weather_forecast = data.get(forecast_key, 'No information available for the specified day.')

    return weather_forecast

if __name__ == "__main__":
    location_url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'
    output_file = 'weather_data.json'

    weather_data = fetch_weather_data(location_url)
    save_to_json(weather_data, output_file)

    json_file = 'weather_data.json'
    user_input_day = input('Enter the day for the weather forecast (e.g., "Today", "Tonight", "Wednesday"): ')

    weather_forecast = get_value_from_json(json_file, user_input_day)
    print(f'Weather Forecast for {user_input_day}: {weather_forecast}')

