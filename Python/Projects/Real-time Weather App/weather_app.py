# API is from:
# • openweathermap.org

# Requirements:
# • PYTHON LANGUAGE
# • terminal~ pip install tkinter
# • terminal~ pip install requests

import tkinter as tk
import requests

from tkinter import ttk


class WeatherAPI:

    API_KEY = '116a4dc8e408d5c2a030d629cc1be768'
    CITY = ''
    API_DATA = {}
    background = 'lightblue'


    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Weather API by Abj :p")
        self.window.configure(background= WeatherAPI.background)
        self.tkUI()


    def tkUI(self):

        def data_button_func():

            def data_handler():

                def label_resetter():
                        self.weathertemperature_label_var.set("")
                        self.weathertemperature_label.configure(font= 'calibri 1', foreground= "darkgreen")

                        self.emoji_label_var.set("")
                        self.emoji_label.configure(font= 'Seguiemj 1')

                        self.weatherdescription_label_var.set("")
                        self.weathertemperature_label.configure(font= 'calibri 1')


                def api_data(city, api_key):
                    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
                    response = requests.get(url)
                    return response.json()


                def exception_handler(weather_connectivity):
                    match int(weather_connectivity):
                        case 400000:
                            self.weathertemperature_label_var.set(f"Error {weather_connectivity}: No API subscription!")
                            self.weathertemperature_label.configure(font= 'calibri 18', foreground="red")
                        case 400:
                            self.weathertemperature_label_var.set(f"Error {weather_connectivity}: Can't be empty!")
                            self.weathertemperature_label.configure(font= 'calibri 18', foreground="red")
                        case 401:
                            self.weathertemperature_label_var.set(f"Error {weather_connectivity}: API is not active!")
                            self.weathertemperature_label.configure(font= 'calibri 18', foreground="red")
                        case 404:
                            self.weathertemperature_label_var.set(f"Error {weather_connectivity}: Wrong city name!")
                            self.weathertemperature_label.configure(font= 'calibri 18', foreground="red")
                        case 429:
                            self.weathertemperature_label_var.set(f"Error {weather_connectivity}: Too many requests!")
                            self.weathertemperature_label.configure(font= 'calibri 18', foreground="red")
                        case _:
                            self.weathertemperature_label_var.set(f"Error {weather_connectivity}: ?")
                            self.weathertemperature_label.configure(font= 'calibri 18', foreground="red")
                

                    if 500 <= int(weather_connectivity) <= 504:
                        self.weathertemperature_label_var.set(f"Error {weather_connectivity}: Please contact API managers!")
                        self.weathertemperature_label.configure(font= 'calibri 18', foreground= 'red')
              
                
                def handler():

                    def var_assigner(weather_temperature, weather_icon, weather_description):

                        def icon_assigner(weather_icon):
                            match weather_icon:
                                case 'Thunderstorm':
                                    return '     ⛈️'
                                
                                case 'Drizzle':
                                    return '     ☔'
                                
                                case 'Rain':
                                    return '     🌧️'
                                
                                case 'Snow':
                                    return '     🌨️'
                                
                                case 'Clear':
                                    return '     ☀️'
                                
                                case 'Clouds':
                                    return '     ☁️'
                                
                                case 'Mist':
                                    return '     😶‍🌫️'
                                
                                case 'Smoke':
                                    return '     😤'
                                
                                case 'Haze':
                                    return '     ☃️'
                                
                                case 'Fog':
                                    return '     😶‍🌫️'
                                
                                case 'Sand':
                                    return '     💨'
                                
                                case 'Dust':
                                    return '     💨'
                                
                                case 'Ash':
                                    return '     🌋'
                                
                                case 'Squall':
                                    return '     ❄️'
                                
                                case 'Tornado':
                                    return '     🌪️'


                        self.weathertemperature_label_var.set(f"{weather_temperature:.1f}°C")
                        self.weathertemperature_label.configure(font= 'calibri 28')

                        self.emoji_label_var.set(icon_assigner(weather_icon))
                        self.emoji_label.configure(font= 'Seguiemj 100')

                        self.weatherdescription_label_var.set(f"{weather_description}")
                        self.weatherdescription_label.configure(font= 'calibri 24')


                    weather_data = WeatherAPI.API_DATA
                    weather_connectivity = weather_data['cod']


                    if weather_connectivity == 200: # Successful API connection
                        weather = weather_data['weather'][0]
                        weather_temperature = weather_data['main']['temp'] - 272.15        
                        weather_icon_info = weather['main']
                        weather_description = weather['description']

                        var_assigner(weather_temperature, weather_icon_info, weather_description)


                    else:
                        exception_handler(weather_connectivity)


                label_resetter()
                WeatherAPI.CITY = self.entry_box.get()
                WeatherAPI.API_DATA = api_data(WeatherAPI.CITY, WeatherAPI.API_KEY)
                handler()


            data_handler()
        

        # Widgets
        self.frame = tk.Frame(master = self.window, background= WeatherAPI.background)
        self.title_label = ttk.Label(self.frame, text= "Enter a city name !", font= "calibri 32", foreground= "blue", anchor= 'center', background= WeatherAPI.background)
        self.entry_box = ttk.Entry(self.frame, font= "calibri 28", justify= "center", width= 30)
        self.data_button = ttk.Button(self.frame, text= "Check!", command= data_button_func)
        self.weathertemperature_label_var = tk.StringVar()
        self.weathertemperature_label = ttk.Label(self.frame, textvariable= self.weathertemperature_label_var, font= "calibri 1", foreground="darkgreen", anchor='center', background= WeatherAPI.background)
        self.emoji_label_var = tk.StringVar()
        self.emoji_label = tk.Label(self.frame, font= 'Seguiemj 1', textvariable= self.emoji_label_var, foreground='red', justify= "center", background= WeatherAPI.background)
        self.weatherdescription_label_var = tk.StringVar()
        self.weatherdescription_label = ttk.Label(self.frame, font= "calibri 1", foreground="darkgreen", anchor='center', textvariable= self.weatherdescription_label_var, background= WeatherAPI.background)

        self.frame.pack(padx=50, pady=20)
        self.title_label.grid(row=0,column=0, sticky= 'news', pady=5)
        self.entry_box.grid(row=1, column=0, sticky= 'news', pady=5)
        self.data_button.grid(row=2, column=0, sticky= 'news', pady=5)
        self.weathertemperature_label.grid(row=3, column=0, sticky= 'news')
        self.emoji_label.grid(row=4, column=0, sticky= 'news')
        self.weatherdescription_label.grid(row=5, column=0, sticky= 'news')


if __name__ == "__main__":
    app = WeatherAPI()
    app.window.mainloop()