import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data=np.random.randn(1000)
sns.histplot(data,kde=True)
plt.title("Histgram and Density")
plt.show()