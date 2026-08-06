#Program 2 in IB Reading a JSON file.. using read_json()

import pandas as pd

df = pd.read_json("students.json")

#Display

print("Students Data..")
print(df)