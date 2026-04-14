import tkinter as tk
import requests

# Try with your own API key

API_KEY = "YOUR_API_KEY"

def get_weather():
    city = city_entry.get()

    if city == "" or city == "Enter city name":
        result_label.config(text="Please enter a valid city!", fg="red")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result_label.config(
                text=f"🌡️ Temperature: {temp} °C\n\n"
                     f"☁️ Condition: {weather}\n\n"
                     f"💧 Humidity: {humidity} %\n\n"
                     f"🌬️ Wind Speed: {wind} m/s",
                fg="white",
                justify="left"
            )
        else:
            result_label.config(text="City not found!", fg="red")

    except:
        result_label.config(text="Error fetching data!", fg="red")


# 🔹 Placeholder functions
def on_entry_click(event):
    if city_entry.get() == "Enter city name":
        city_entry.delete(0, "end")
        city_entry.config(fg="black")

def on_focus_out(event):
    if city_entry.get() == "":
        city_entry.insert(0, "Enter city name")
        city_entry.config(fg="grey")


# 🖥️ Window
window = tk.Tk()
window.title("Weather App 🌦️")
window.geometry("420x400")
window.configure(bg="#1e1e2f")

# 🏷️ Title
title = tk.Label(
    window,
    text="Weather App 🌦️",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=15)

# 📥 Entry with placeholder
city_entry = tk.Entry(window, width=30, font=("Arial", 12), fg="grey")
city_entry.insert(0, "Enter city name")
city_entry.bind("<FocusIn>", on_entry_click)
city_entry.bind("<FocusOut>", on_focus_out)
city_entry.pack(pady=10, ipady=5)

# 🔘 Button
search_btn = tk.Button(
    window,
    text="Get Weather",
    command=get_weather,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    width=15
)
search_btn.pack(pady=15)

# 📊 Result box (clean spacing)
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white",
    justify="left",
    anchor="w"
)
result_label.pack(pady=20, padx=20)

window.mainloop()
