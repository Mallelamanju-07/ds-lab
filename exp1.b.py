# Experiment 1B Writing and Pursing JSON Data..


import pandas as pd
student_data = {
    "Roll No":[101,102,103,104],
    "Name": ["Anusha","Babitha","Charitha","Deepika"],
    "Department":["IT","IT","CSE","DS"],
    "Marks":[89,92,88,85]
}
df = pd.DataFrame(student_data)
df.to_json(
    "students.json",
    orient = "records",
    index = 4
)
print("JSON file created sucessfully")
