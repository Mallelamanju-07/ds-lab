import pandas as pd
data = {
    'Name': ['Manju', 'Harsha', 'Vignesh', 'Guru', 'Paul', 'Umar', 'Sai', 'vara'],
    'Department': ['CSE', 'CSE', 'ECE', 'ECE', 'CSE', 'ECE', 'CSE', 'ECE'],
    'Year': [3, 2, 3, 3, 2, 3, 3, 2],
    'Marks': [98, 90, 88, 89, 95, 85, 81, 99]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


print("\n1. Group by Department:")

group1 = df.groupby('Department')

for name, group in group1:
    print("\nDepartment:", name)
    print(group)

print("\nAverage Marks by Department:")
print(df.groupby('Department')['Marks'].mean())

print("\n2. Group by Department and Year:")

group2 = df.groupby(['Department', 'Year'])

for name, group in group2:
    print("\nGroup:", name)
    print(group)
print("\nAverage Marks by Department and Year:")
print(df.groupby(['Department', 'Year'])['Marks'].mean())