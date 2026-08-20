#reading an excel file
import pandas as pd
df=pd.read_excel("students.xlsx",sheet_name="Students_Details")
print("data read from excek file:")
print(df)