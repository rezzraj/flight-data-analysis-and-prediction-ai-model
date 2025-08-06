import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns



#loading the file
df=pd.read_csv('airlines_flights_data.csv')
df=df.dropna()



#total number of cities
print(f'No of cities being analysed {df['source_city'].unique()}')
print(f'no of airline being analysed {df['airline'].unique()} ')
print(f'no of seat classes  {df['class'].unique()} ')
print(f'departure times  {df['departure_time'].unique()} ')
#comparing different values by plotting graphs

#ariline vs duration
max_dur=df.groupby('airline')['duration'].max().reset_index()
sns.barplot(x='airline', y='duration', data=max_dur)
plt.title('Airline Vs Duration ', fontsize='16', fontweight='bold')
plt.xlabel('all airlines')
plt.ylabel('duration in hours')
plt.show()

#duration vs price
grouped=df.groupby('duration')['price'].mean().reset_index()
sns.histplot(data=grouped, x= 'duration', y='price')
plt.show()

#airline vs price
sns.barplot(data=df, x='airline',y='price')
plt.show()

#no of flights for all airlines
sns.countplot(data=df, x= 'airline')
plt.title('no of flights count for each airline')
plt.show()

#which airline has the longest flight
max_duration=df['duration'].max()
max_duration_row=df[df['duration']==max_duration]
print(f'{max_duration_row.iloc[0]['airline']} Had the longest flight')

#max value for money
df['value']=df['duration']/df['price']
effi=df.groupby('airline')['price'].mean().sort_values().reset_index()
print(f'Avg Price of each airline \n{effi}')
most_value_for_money=effi.loc[0,'airline']
print(f'{most_value_for_money} has the best value for money')