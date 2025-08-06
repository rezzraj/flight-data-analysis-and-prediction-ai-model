import pandas as pd
import sklearn
from numpy.ma.core import indices
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import seaborn as sns

#loading the file
df=pd.read_csv('airlines_flights_data.csv')
df=df.dropna()
print(df.columns)

#converting all strings to numbers for model to train on
dfm=pd.get_dummies(df,columns=['airline','source_city','class','departure_time','destination_city'],drop_first=True)
dfm=dfm.sample(n=10000,random_state=42)

#removing useless quantities from training data
x=dfm.drop(['price','flight','stops','arrival_time','index','duration'],axis=1)
y=dfm['price']

#splitting data into training vs testing
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)



#training Random forest regressor model
model=RandomForestRegressor()
model.fit(x_train,y_train)

#feature importance for first model
importance=model.feature_importances_
features=x_train.columns
indices= importance.argsort()[::-1]

#plotting
plt.figure(figsize=(10,6))
plt.barh(features[indices][:15], importance[indices][:15])
plt.title('top 15 factors affecting price (descending order)')
plt.tight_layout()

plt.show()




#training linear regression model
model2=LinearRegression()
model2.fit(x_train,y_train)




#predicting the output first model
y_pred=model.predict(x_test)

#predicting the output second model
y_pred2=model2.predict(x_test)

#finding accuracy
print(f'accuracy Random forest regressor model: {round((r2_score(y_test,y_pred)),2)}')
print(f'error margin in Rupees Random forest regressor model : {round((mean_absolute_error(y_test,y_pred)),2)}')

print(f'accuracy Random liner regression model: {round((r2_score(y_test,y_pred2)),2)}')
print(f'error margin in Rupees Random liner regression model : {round((mean_absolute_error(y_test,y_pred2)),2)}')


#testing by user input
airlineInp=input('Which airline u want SpiceJet AirAsia Vistara GO_FIRST Indigo Air_India: ')
sourceCityinp=input('enter the source city(Delhi Mumbai Bangalore Kolkata Hyderabad Chennai: ').capitalize()
departuretimeinp=input('enter departure time(Evening Early_Morning Morning Afternoon Night Late_Night): ').capitalize()
destinationCinp=input('enter destination: ').capitalize()
classinp=input('which class u flying(economy, business) : ').capitalize()
dayslinp=input('how prior are u booking (no of days left): ')

sample=pd.DataFrame([{'airline':airlineInp,
                      'source_city':sourceCityinp,
                      'departure_time':departuretimeinp,
                      'destination_city':destinationCinp,
                      'class':classinp,
                      'days_left':dayslinp}])

sample_encoded = pd.get_dummies(sample)
sample_encoded = sample_encoded.reindex(columns=x_train.columns, fill_value=0)
predicted_price1 = model.predict(sample_encoded)[0]
predicted_price2 = model2.predict(sample_encoded)[0]
print("Predicted Ticket Price random forest regressor:", round(predicted_price1,2))
print("Predicted Ticket Price liner regressor:", round(predicted_price2,2))
