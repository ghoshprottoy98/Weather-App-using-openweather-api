import json
import tkinter as tk
from tkinter import font
import requests
import time

#get weather API
def getWeather(canvas):
    city = textField.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+ city +"&APPID=d5199b9b1dbe981c7a5ec22e425452f7"
    json_data = requests.get(api).json()

    #get data API
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    #output data
    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


#create canvas
canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title('Weather APP')

#set font and size
f = ('arial', 16, 'bold')
t = ('arial', 30, 'bold')
s = ('arial', 20, 'bold')

label3=tk.Label(canvas, font=s, text='Enter City Name Below')
label3.pack() 

#create textfield to define city
textField = tk.Entry(canvas, font = t)
textField.pack(pady= 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()
