import os

file_path = "Data/data.csv"
if os.path.exists(file_path):
    print("File exists")
else : 
    print("File does not exist")