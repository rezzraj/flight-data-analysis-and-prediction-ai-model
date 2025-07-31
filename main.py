import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


df=pd.read_csv('airlines_flights_data.csv')

#comparing different values by plotting graphs


#ariline vs duration
sns.barplot(x='airline', y='duration', data=df)
plt.show()

#duration vs price
sns.scatterplot(data=df,x='duration',y='price')
plt.show()

#airline vs price
sns.barplot(data=df, x='airline',y='price')
plt.show()

#airline vs no of flights
airline_counts= df['airline'].value_counts().reset_index()
airline_counts.columns=['airline','flight_count']

#no of flights for all airlines
print(airline_counts)
sns.barplot(data=airline_counts, x=airline_counts.airline, y=airline_counts.flight_count)
plt.show()

#which airline has the longest flight
max_duration=df['duration'].max()
max_duration_row=df[df['duration']==max_duration]


print(max_duration_row.iloc[0]['airline'])