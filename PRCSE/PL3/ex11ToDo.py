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

    # Extract the text content of the "Detailed Forecast" section
    detailed_forecast_text = detailed_forecast.get_text(strip=True)
    print(f'det: {detailed_forecast_text}')
    # Split the detailed forecast into sentences
    forecast_sentences = [sentence.strip() for sentence in detailed_forecast_text.split('.') if sentence]
    #print(f'Content: {forecast_sentences}')
    # Extract relevant information for Today and Tonight
    today_forecast = forecast_sentences[0]
    tonight_forecast = forecast_sentences[1]

    # Create the desired JSON structure
    extracted_data = {
        'Today': today_forecast,
        'Tonight': tonight_forecast
    }

    return extracted_data

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    location_url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'
    output_file = 'weather_data.json'

    weather_data = fetch_weather_data(location_url)
    save_to_json(weather_data, output_file)

    print(f'The weather data has been successfully fetched and saved to {output_file}.')

import json

def get_weather_forecast(json_file, day):
    with open(json_file, 'r') as json_file:
        data = json.load(json_file)

    # Retrieve the weather forecast for the given day
    forecast_key = f'forecast_{day}'
    
    weather_forecast = data.get(forecast_key, 'No information available for the specified day.')

    return weather_forecast

if __name__ == "__main__":
    json_file = 'weather_data.json'
    user_input_day = input('Enter the day for the weather forecast (e.g., "Today", "Tonight", "Wednesday"): ')

    weather_forecast = get_weather_forecast(json_file, user_input_day)
    print(f'Weather Forecast for {user_input_day}: {weather_forecast}')

