import re
text="DS is\t very \n useful"
split_text=re.split(r'\s+',text)
print(split_text)