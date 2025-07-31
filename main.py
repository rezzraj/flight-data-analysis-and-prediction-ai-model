import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df=pd.read_csv('C:\\Users\\akshi\\Downloads\\all stuff\\airlines_flights_data.csv')

sns.scatterplot(x='airline', y='duration', data=df)
plt.show()


sns.scatterplot(data=df,x='duration',y='price')
plt.show()


sns.barplot(data=df, x='airline',y='price')
plt.show()