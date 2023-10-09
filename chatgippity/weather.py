import requests
import datetime

def get_weather(city, api_key):
    # Make a request to the OpenWeather API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        timezone_offset = data['timezone']
        
        # Get current time and date in the city's timezone
        current_time_utc = datetime.datetime.utcnow()
        city_time = current_time_utc + datetime.timedelta(seconds=timezone_offset)
        
        # Print the weather, time, date, and timezone
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Time: {city_time.strftime('%H:%M:%S')}")
        print(f"Date: {city_time.strftime('%Y-%m-%d')}")
        print(f"Time Zone: UTC{timezone_offset/3600:+.2f}")
    else:
        print("Error fetching data from OpenWeather API")

if __name__ == "__main__":
    api_key = "12b846ac32b7152485655d8fea44adbc"  # Replace with your OpenWeather API key
    city = input("Enter a city name: ")
    get_weather(city, api_key)