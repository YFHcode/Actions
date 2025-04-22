import requests 
import pandas as pd
import json

def getData(url):
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        data = pd.DataFrame(data)
        data.to_csv('Data/data.csv', index=False)
        print("Data saved to data.csv")
    else:
        print("Failed to retrieve data. Status code:", data.status_code)

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    getData(url)
# This code retrieves data from a given URL, converts it to a pandas DataFrame, and saves it as a CSV file. It also checks if the request was successful before proceeding with the conversion and saving process.