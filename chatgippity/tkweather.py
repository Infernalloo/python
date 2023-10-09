import tkinter as tk
from tkinter import Entry, Button, Label, Frame
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
        
        # Update the label with weather, time, date, and timezone information
        result_label.config(text=f"Weather in {city}: {weather_description}\n"
                                  f"Temperature: {temperature}°C\n"
                                  f"Time: {city_time.strftime('%H:%M:%S')}\n"
                                  f"Date: {city_time.strftime('%Y-%m-%d')}\n"
                                  f"Time Zone: UTC{timezone_offset/3600:+.2f}")
    else:
        result_label.config(text="Error fetching data from OpenWeather API")

def get_weather_from_input(event=None):
    city = city_entry.get()
    api_key = "12b846ac32b7152485655d8fea44adbc"  # Replace with your OpenWeather API key
    get_weather(city, api_key)

# Create the main Tkinter window
root = tk.Tk()
root.title("Weather App")
root.geometry("640x480")

# Create and place input elements
input_frame = Frame(root, bd=3, relief="groove")
input_frame.pack(pady=10, padx=10, fill="x")

city_label = Label(input_frame, text="Enter a city name:", font=("JetBrainsMono Nerd Font", 14))
city_label.pack(pady=5)
city_entry = Entry(input_frame, font=("JetBrainsMono Nerd Font", 14))
city_entry.pack(pady=5)
get_weather_button = Button(input_frame, text="Get Weather", command=get_weather_from_input, font=("JetBrainsMono Nerd Font", 14))
get_weather_button.pack(pady=5)

# Bind the "Enter" key to the button
city_entry.bind("<Return>", get_weather_from_input)

# Create and place result label with individual borders for each line
result_frame = Frame(root, bd=3, relief="groove")
result_frame.pack(pady=10, padx=10, fill="both")

result_label = Label(result_frame, text="", justify="left", font=("JetBrainsMono Nerd Font", 14))
result_label.pack(pady=5, padx=5)

# Start the Tkinter main loop
root.mainloop()