import pandas as pd
student_data={
    "Roll_no":[101,102,103],
    "Name":["Anusha","Babitha","Charitha"],
    "Department":["IT","IT","CSE"],
    "Percentage":[89,92,88]
}
course_data={
    "course_id":["c101","c102","c103"],
    "course_name":["python","datascience","machinelearning"],
    "credits":[4,3,4]
}
student_df=pd.DataFrame(student_data)
course_df=pd.DataFrame(course_data)
with pd.ExcelWriter("college_data.xlsx",engine="openpyxl") as writer:
    student_df.to_excel(writer,sheet_name="Students",index=False)
    course_df.to_excel(writer,sheet_name="Courses",index=False)
print("multiple sheets written to college_data.xlsx")