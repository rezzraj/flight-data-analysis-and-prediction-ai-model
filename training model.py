import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.linear_model import LinearRegression


df=pd.read_csv('airlines_flights_data.csv')
df=df.dropna()

#training the Random forest regressor model


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

sample=pd.DataFrame([{'airline':'Indigo',
                      'source_city':'Delhi',
                      'departure_time':'Night',
                      'destination_city':'Mumbai',
                      'class':'Economy',
                      'days_left':'1'}])

sample_encoded = pd.get_dummies(sample)
sample_encoded = sample_encoded.reindex(columns=x_train.columns, fill_value=0)
predicted_price1 = model.predict(sample_encoded)[0]
predicted_price2 = model2.predict(sample_encoded)[0]
print("Predicted Ticket Price random forest regressor:", round(predicted_price1,2))
print("Predicted Ticket Price liner regressor:", round(predicted_price2,2))
