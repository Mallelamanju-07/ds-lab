
import pandas as pd
student_data = {
    "Roll_No": [101, 102, 103, 104],
    "Name": ["Anusha", "Babitha", "Charitha", "Deepika"],
    "Dept": ["IT", "IT", "CSE", "ECE"],
    "Percentage": [89, 92, 88, 85]
}

df = pd.DataFrame(student_data)
print("Student Data:")
print(df)
df.to_csv("student_output.txt", sep="\t", index=False)

print("Data successfully written to student_output.txt")