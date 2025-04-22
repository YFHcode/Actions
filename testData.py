import os
# This is a test file to check if the data file exists in the specified path
file_path = "Data/data.csv"
if os.path.exists(file_path):
    print("File exists")
else : 
    print("File does not exist.")