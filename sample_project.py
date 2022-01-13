import numpy as np
import matplotlib.pyplot as plt
import math_tools as mt
import seaborn as sns

titanic_df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')
titanic_df.info()

titanic_df.Age.hist()
plt.show()

titanic_corr = titanic_df.corr()
plt.figure(figsize=(10,6))
sns.heatmap(titanic_corr, annot=True)
plt.show()