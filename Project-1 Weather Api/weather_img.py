# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import requests
#
# # API details
# api_key = "541fa51ee47675cbcf3a3cbb7d8c2fdc"
# base_url = "https://api.openweathermap.org/data/2.5/weather?"
#
# # Function to get weather data
# def get_weather():
#     city_name = city_entry.get()
#     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#     response = requests.get(complete_url)
#     data = response.json()
#
#     result_label.config(text="")  # Clear previous results
#
#     if data["cod"] != "404":
#         record = data["main"]
#         current_temperature_kelvin = record["temp"]
#         current_pressure = record["pressure"]
#         current_humidity = record["humidity"]
#         record1 = data["weather"]
#         weather_description = record1[0]["description"]
#         icon_name = record1[0]["icon"]  # Get the icon code
#
#         # Get the selected temperature unit
#         selected_unit = temp_unit.get()
#
#         # Convert temperature based on the selected unit
#         if selected_unit == "C":
#             current_temperature = current_temperature_kelvin - 273.15  # Kelvin to Celsius
#             temperature_str = f"Temperature: {current_temperature:.2f} °C"
#         elif selected_unit == "F":
#             current_temperature = (current_temperature_kelvin - 273.15) * 9/5 + 32  # Kelvin to Fahrenheit
#             temperature_str = f"Temperature: {current_temperature:.2f} °F"
#         else:
#             current_temperature = current_temperature_kelvin
#             temperature_str = f"Temperature: {current_temperature:.2f} K"
#
#         result = (f"{temperature_str}\n"
#                   f"Pressure (in hPa): {current_pressure}\n"
#                   f"Humidity (in %): {current_humidity}\n"
#                   f"Weather: {weather_description.capitalize()}")
#         result_label.config(text=result)
#         load_weather_icon(icon_name)  # Load the corresponding weather icon
#     else:
#         result_label.config(text="City Not Found")
#
# def load_weather_icon(icon_name):
#     try:
#         # Build the URL for the weather icon
#         icon_url = f"http://openweathermap.org/img/wn/{icon_name}@2x.png"
#         icon_image = Image.open(requests.get(icon_url, stream=True).raw)
#         icon_image = icon_image.resize((100, 100), Image.Resampling.LANCZOS)
#         weather_icon = ImageTk.PhotoImage(icon_image)
#         icon_label.config(image=weather_icon)
#         icon_label.image = weather_icon  # Keep a reference to avoid garbage collection
#     except Exception as e:
#         print(f"Error loading icon: {e}")
#         icon_label.config(image='')  # Clear the icon if there's an issue
#
# # Load and resize background image based on current window size
# def update_background_image(event=None):
#     window_width = root.winfo_width()
#     window_height = root.winfo_height()
#     resized_image = image.resize((window_width, window_height), Image.Resampling.LANCZOS)
#     background_image = ImageTk.PhotoImage(resized_image)
#     background_label.config(image=background_image)
#     background_label.image = background_image  # Keep a reference to avoid garbage collection
#
# # Set up the Tkinter window
# root = tk.Tk()
# root.title("Responsive Weather App")
#
# # Set window initial size
# root.geometry("800x600")
#
# # Load the initial background image
# image_path = "https://th.bing.com/th/id/OIP.QXYu8JqMdwfnNnAlDTuoGQHaFN?rs=1&pid=ImgDetMain"  # Path to your uploaded image
# image = Image.open(image_path)
#
# # Set initial background image
# background_image = ImageTk.PhotoImage(image)
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# # Create a frame to center the inputs
# center_frame = ttk.Frame(root, padding=20)
# center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#
# # Create and place the city input label and entry
# city_label = ttk.Label(center_frame, text="Enter city name:", background='white')
# city_label.grid(row=0, column=0, pady=10)
#
# city_entry = ttk.Entry(center_frame, width=20, font=("Arial", 12))
# city_entry.grid(row=0, column=1, pady=10)
#
# # Create a dropdown menu to select temperature unit
# temp_unit = tk.StringVar(value="Kelvin")
# unit_label = ttk.Label(center_frame, text="Select temperature unit:", background='white')
# unit_label.grid(row=1, column=0, pady=10)
#
# unit_dropdown = ttk.Combobox(center_frame, textvariable=temp_unit, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
# unit_dropdown.grid(row=1, column=1, pady=10)
#
# # Create and place the Get Weather button
# get_weather_button = ttk.Button(center_frame, text="Get Weather", command=get_weather)
# get_weather_button.grid(row=2, column=0, columnspan=2, pady=10)
#
# # Create a label to display the results
# result_label = ttk.Label(center_frame, text="", background='white', wraplength=300, font=("Arial", 12))
# result_label.grid(row=3, column=0, columnspan=2, pady=10)
#
# # Create a label for the weather icon
# icon_label = tk.Label(center_frame, background='white')
# icon_label.grid(row=4, column=0, columnspan=2, pady=10)
#
# # Bind the window resize event to dynamically adjust the background image
# root.bind('<Configure>', update_background_image)
#
# # Start the Tkinter main loop
# root.mainloop()

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO  # Import BytesIO

# API details
api_key = "541fa51ee47675cbcf3a3cbb7d8c2fdc"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# Function to get weather data
def get_weather():
    city_name = city_entry.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()

    result_label.config(text="")  # Clear previous results

    if data["cod"] != "404":
        record = data["main"]
        current_temperature_kelvin = record["temp"]
        current_pressure = record["pressure"]
        current_humidity = record["humidity"]
        record1 = data["weather"]
        weather_description = record1[0]["description"]
        icon_name = record1[0]["icon"]  # Get the icon code

        # Get the selected temperature unit
        selected_unit = temp_unit.get()

        # Convert temperature based on the selected unit
        if selected_unit == "Celsius":
            current_temperature = current_temperature_kelvin - 273.15  # Kelvin to Celsius
            temperature_str = f"Temperature: {current_temperature:.2f} °C"
        elif selected_unit == "Fahrenheit":
            current_temperature = (current_temperature_kelvin - 273.15) * 9/5 + 32  # Kelvin to Fahrenheit
            temperature_str = f"Temperature: {current_temperature:.2f} °F"
        else:
            current_temperature = current_temperature_kelvin
            temperature_str = f"Temperature: {current_temperature:.2f} K"

        result = (f"{temperature_str}\n"
                  f"Pressure (in hPa): {current_pressure}\n"
                  f"Humidity (in %): {current_humidity}\n"
                  f"Weather: {weather_description.capitalize()}")
        result_label.config(text=result)
        load_weather_icon(icon_name)  # Load the corresponding weather icon
    else:
        result_label.config(text="City Not Found")

def load_weather_icon(icon_name):
    try:
        # Build the URL for the weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_name}@2x.png"
        icon_image = Image.open(requests.get(icon_url, stream=True).raw)
        icon_image = icon_image.resize((100, 100), Image.Resampling.LANCZOS)
        weather_icon = ImageTk.PhotoImage(icon_image)
        icon_label.config(image=weather_icon)
        icon_label.image = weather_icon  # Keep a reference to avoid garbage collection
    except Exception as e:
        print(f"Error loading icon: {e}")
        icon_label.config(image='')  # Clear the icon if there's an issue

# Load and resize background image based on current window size
def update_background_image(event=None):
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    resized_image = image.resize((window_width, window_height), Image.Resampling.LANCZOS)
    background_image = ImageTk.PhotoImage(resized_image)
    background_label.config(image=background_image)
    background_label.image = background_image  # Keep a reference to avoid garbage collection

# Set up the Tkinter window
root = tk.Tk()
root.title("Responsive Weather App")

# Set window initial size
root.geometry("800x600")

# Load the initial background image
image_path = "https://th.bing.com/th/id/OIP.QXYu8JqMdwfnNnAlDTuoGQHaFN?rs=1&pid=ImgDetMain"  # URL of your image
response = requests.get(image_path)
image = Image.open(BytesIO(response.content))  # Use BytesIO to open the image from the response content

# Set initial background image
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to center the inputs
center_frame = ttk.Frame(root, padding=20)
center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create and place the city input label and entry
city_label = ttk.Label(center_frame, text="Enter city name:", background='white')
city_label.grid(row=0, column=0, pady=10)

city_entry = ttk.Entry(center_frame, width=20, font=("Arial", 12))
city_entry.grid(row=0, column=1, pady=10)

# Create a dropdown menu to select temperature unit
temp_unit = tk.StringVar(value="Kelvin")
unit_label = ttk.Label(center_frame, text="Select temperature unit:", background='white')
unit_label.grid(row=1, column=0, pady=10)

unit_dropdown = ttk.Combobox(center_frame, textvariable=temp_unit, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
unit_dropdown.grid(row=1, column=1, pady=10)

# Create and place the Get Weather button
get_weather_button = ttk.Button(center_frame, text="Get Weather", command=get_weather)
get_weather_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a label to display the results
result_label = ttk.Label(center_frame, text="", background='white', wraplength=300, font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Create a label for the weather icon
icon_label = tk.Label(center_frame, background='white')
icon_label.grid(row=4, column=0, columnspan=2, pady=10)

# Bind the window resize event to dynamically adjust the background image
root.bind('<Configure>', update_background_image)

# Start the Tkinter main loop
root.mainloop()