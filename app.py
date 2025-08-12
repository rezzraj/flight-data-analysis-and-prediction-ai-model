import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
df = pd.read_csv('airlines_flights_data.csv')
df = df.dropna()

# Encoding categorical variables
dfm = pd.get_dummies(df, columns=['airline', 'source_city', 'class', 'departure_time', 'destination_city'], drop_first=True)
dfm = dfm.sample(n=10000, random_state=42)

# Features & Target
x = dfm.drop(['price', 'flight', 'stops', 'arrival_time', 'index', 'duration'], axis=1)
y = dfm['price']

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train models
model = RandomForestRegressor()
model.fit(x_train, y_train)

model2 = LinearRegression()
model2.fit(x_train, y_train)

# Predictions & Metrics
y_pred = model.predict(x_test)
y_pred2 = model2.predict(x_test)

r2_rf = round(r2_score(y_test, y_pred), 2)
mae_rf = round(mean_absolute_error(y_test, y_pred), 2)

r2_lr = round(r2_score(y_test, y_pred2), 2)
mae_lr = round(mean_absolute_error(y_test, y_pred2), 2)

# Streamlit UI
st.title("✈ Flight Price Prediction App")
st.write(f"**Random Forest R²:** {r2_rf} | **MAE:** ₹{mae_rf}")
st.write(f"**Linear Regression R²:** {r2_lr} | **MAE:** ₹{mae_lr}")

# User input form
st.subheader("Enter Flight Details")
airlineInp = st.selectbox("Airline", ['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India'])
sourceCityinp = st.selectbox("Source City", ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
departuretimeinp = st.selectbox("Departure Time", ['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'])
destinationCinp = st.selectbox("Destination City", ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
classinp = st.selectbox("Class", ['Economy', 'Business'])
dayslinp = st.number_input("Days Left for Departure", min_value=0, step=1)

# Prediction button
if st.button("Predict Price"):
    sample = pd.DataFrame([{
        'airline': airlineInp,
        'source_city': sourceCityinp,
        'departure_time': departuretimeinp,
        'destination_city': destinationCinp,
        'class': classinp,
        'days_left': dayslinp
    }])

    # One-hot encode sample to match training features
    sample_encoded = pd.get_dummies(sample)
    sample_encoded = sample_encoded.reindex(columns=x_train.columns, fill_value=0)

    # Predictions
    predicted_price1 = model.predict(sample_encoded)[0]
    predicted_price2 = model2.predict(sample_encoded)[0]

    st.success(f"Random Forest Prediction: ₹{round(predicted_price1, 2)}")
    st.success(f"Linear Regression Prediction: ₹{round(predicted_price2, 2)}")

# Feature Importance Plot
importance = model.feature_importances_
features = x_train.columns
indices = importance.argsort()[::-1]

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(features[indices][:15], importance[indices][:15])
ax.set_title('Top 15 Factors Affecting Price')
st.pyplot(fig)
