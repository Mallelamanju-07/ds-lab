#creating and writing to excel file
import pandas as pd
student_data={
    "Roll_no":[101,102,103,104],
    "Name":["Anusha","Babitha","Charitha","Deppika"],
    "Department":["IT","IT","CSE","ECE"],
    "Percentage":[89,92,88,85]
}
df=pd.DataFrame(student_data)
df.to_excel("students.xlsx",sheet_name="Students_Details",index=False)
print("data successfullly written to students.xlsx")