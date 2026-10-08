import pandas as pd
data = {
    'Department': ['CSE', 'CSE', 'CSE', 'ECE', 'ECE', 'ECE',
                   'EEE', 'EEE', 'EEE'],
    'Marks': [85, 80, 90, 73, 75, 95, 93, 92, 100],
    'Attendance': [90, 82, 85, 83, 92, 98, 90, 88, 100]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
result = df.groupby('Department').aggregate({
    'Marks': ['sum', 'mean', 'std'],
    'Attendance': ['sum', 'mean', 'std']
})
print("\nAverage Marks by Department and Year:")
print(df.groupby(['Department','Year'])['Marks'].mean())