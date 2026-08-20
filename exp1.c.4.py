import pandas as pd
excel_data=pd.read_excel("college_data.xlsx",sheet_name=None)
print("data read from excel file:")
print("Available sheets:")
print(excel_data.keys())
print("\nstudent_sheet:")
print(excel_data["Students"])
print("\ncourse_sheet:")
print(excel_data["Courses"])