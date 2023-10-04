from tkinter import *
import requests

def weather_forcast():
    api_key = 'b94486085331eff2b6fc6316d8951cf2'#OpenWeatherMap API key
    city_name = city_name_entry.get()# taking city name from entry

    # Making an API request to retrieve weather data based on the user's input
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "imperial"
    }

    response = requests.get(base_url, params=params)

    #checking if the response status code is 200 (OK)
    if response.status_code == 200:
        weather_data = response.json() #parse the JSON response to extract weather data.

    else:
        result_label.config(text="Error fetching weather data.")
        return

    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_description = weather_data['weather'][0]['description']

        result_label.config(text=f'''Weather of {city_name}:
        
Temperature: {temperature} °F

Humidity: {humidity} %

Wind Speed: {wind_speed} m/hr

Description: {weather_description.capitalize()}
''')

    else:
        result_label.config(text='No weather data to display')

root = Tk()#creating GUI main window

root.title('Weather Forcast')
root.wm_iconbitmap('icon.ico')

#create a image label for application title
image = PhotoImage(file='new.png')
image_label = Label(image=image)
image_label.grid(row=0, column=1, padx=2, pady=2)

# create a label for the application title
label = Label(text='WEATHER FORCAST', font='Bold 20')
label.grid(row=0, column=2, padx=2, pady=2)

root.geometry('500x600')

label = Label(text="City Name:", font=15)
label.grid(row=1, column=1, padx=2, pady=2)
city_name_entry = Entry(root, font=20, borderwidth=2, relief='groove', bg='sky blue',) #taking input
city_name_entry.grid(row=1, column=2, padx=2, pady=2)

#creating "Search" button that calls the weather_forcast() function when clicked
button = Button(root, text='Search', command=weather_forcast, bg='sky blue', font='bold', relief='groove', borderwidth=2)
button.grid(row=2, column=2, padx=2, pady=4)

result_label = Label(root, text='', font='bold 20')
result_label.grid(row=3, column=2, padx=2, pady=2)

root.mainloop()

