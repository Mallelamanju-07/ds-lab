import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'Category':['A','B','C'],'values':[10,20,15]})
df.plot(kind='bar',x='Category',y='values')
plt.title("Bar plot")
plt.show()