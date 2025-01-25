import tkinter as tk
from tkinter import ttk
import requests
import json

api_key = "541fa51ee47675cbcf3a3cbb7d8c2fdc"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather():
    city_name = city_entry.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()

    result_tree.delete(*result_tree.get_children())

    if data["cod"] != "404":
        record = data["main"]
        current_temperature_kelvin = record["temp"]
        current_pressure = record["pressure"]
        current_humidity = record["humidity"]
        record1 = data["weather"]
        weather_description = record1[0]["description"]

        unit = unit_var.get()
        
        if unit == "Celsius":
            current_temperature = round(current_temperature_kelvin - 273.15, 2)
        elif unit == "Fahrenheit":
            current_temperature = round((current_temperature_kelvin - 273.15) * 9/5 + 32, 2)
        else:
            current_temperature = current_temperature_kelvin

        result_tree.insert("", "end", text="Temperature", values=(f"{current_temperature} {unit}",))
        result_tree.insert("", "end", text="Atmospheric Pressure", values=(f"{current_pressure} hPa",))
        result_tree.insert("", "end", text="Humidity", values=(f"{current_humidity}%",))
        result_tree.insert("", "end", text="Description", values=(weather_description,))
    else:
        result_tree.insert("", "end", text="Error", values=("City Not Found",))

root = tk.Tk()
root.title("Enhanced Weather App")
root.geometry("400x300")

style = ttk.Style()
style.theme_use('clam')

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=10)

result_frame = ttk.Frame(main_frame)
result_frame.pack(fill=tk.BOTH, expand=True)

city_label = ttk.Label(input_frame, text="Enter city name:")
city_label.pack(side=tk.LEFT, padx=5)
city_entry = ttk.Entry(input_frame, width=20)
city_entry.pack(side=tk.LEFT, padx=5)

get_weather_button = ttk.Button(input_frame, text="Get Weather", command=get_weather)
get_weather_button.pack(side=tk.LEFT, padx=5)

unit_var = tk.StringVar(root)
unit_var.set("Kelvin")
unit_options = ["Kelvin", "Celsius", "Fahrenheit"]
unit_menu = ttk.OptionMenu(input_frame, unit_var, "Kelvin", *unit_options)
unit_menu.pack(side=tk.LEFT, padx=5)

result_tree = ttk.Treeview(result_frame, columns=("Value"), show="tree")
result_tree.pack(fill=tk.BOTH, expand=True)

result_tree.heading("#0", text="Parameter")
result_tree.heading("Value", text="Value")

root.mainloop()
