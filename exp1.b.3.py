# Parsing JSON Data from a String

import pandas as pd

from io import StringIO

json_data = """
[
    {
        "Roll_no": 101,
        "Name": "Anusha",
        "Marks":89
    },
        
        
    {
            "Roll_no": 102,
            "Name": "Babitha",
            "Marks":92
     },
    
    {
            "Roll_no": 103,
            "Name": "Charitha",
            "Marks":88
    },
        
    {
            "Roll_no": 104,
            "Name": "Deepika",
            "Marks":93
    }
]
"""

df = pd.read_json(StringIO(json_data))
print("Parsed JSON Data")
print(df)