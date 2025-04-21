import requests 
import pandas as pd
import json

def getData(url):
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        data = pd.DataFrame(data)
        data.to_csv('C:/Users/lenovo/Desktop/Actions/Data/data.csv', index=False)
        print("Data saved to data.csv")
    else:
        print("Failed to retrieve data. Status code:", data.status_code)

if __name__ == "__main__":
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    getData(url)