The Dataset from kaggle (https://www.kaggle.com/datasets/rohitgrewal/airlines-flights-data/data)
Airlines Flights Dataset for Different Cities
The Flights Booking Dataset of various Airlines is a scraped datewise from a famous website in a structured format. 
The dataset contains the records of flight travel details between the cities in India. Here, multiple features are present like Source & Destination City, Arrival & Departure Time, Duration & Price of the flight etc.
This data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame.
This analyse will be helpful for those working in Airlines, Travel domain.


These are the main Features/Columns available in the dataset :

1) Airline: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.
2) Flight: Flight stores information regarding the plane's flight code. It is a categorical feature.
3) Source City: City from which the flight takes off. It is a categorical feature having 6 unique cities.
4) Departure Time: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.
5) Stops: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.
6) Arrival Time: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.
7) Destination City: City where the flight will land. It is a categorical feature having 6 unique cities.
8) Class: A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.
9) Duration: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.
10) Days Left: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.
11) Price: Target variable stores information of the ticket price.


project info-

TRAINING MODELS
I have trained two models from Sci-kit learn database namely liner regression model and random forest generator model, While also comparing and analysing accuracy and margin of error by each.
the model require inputs ('airline','source_city','class','departure_time','destination_city', etc) and will predict the price of the airline only among few ('Delhi' 'Mumbai' 'Bangalore' 'Kolkata' 'Hyderabad' 'Chennai') cities.
Also comparing LR model with RFR (RFR better)

VISUALIZATION & ANALYSIS
I have also analysed various parameters and compared them with one another and plotted a graph using Seaborn library, i also extracted some meaningful information like no of cities being analyzed in the dataset,
which airline had the longest flight, which airline is the most value for money, which is the most expensive airline and avg price of each airline 





Output=


TRAINING MODELS

accuracy Random forest regressor model: 0.91

error margin in Rupees Random forest regressor model : 3676.83

accuracy Random liner regression model: 0.9

error margin in Rupees Random liner regression model : 4461.07

Predicted Ticket Price random forest regressor: 13506.51

Predicted Ticket Price liner regressor: 7173.56





VISUALIZATION & ANALYSIS

the graphs are provided in the visualization folder attached

Air_India Had the longest flight

Avg Price of each airline -
    AirAsia = 4091.072742,
    
    Indigo = 5324.216303, 
    
    GO_FIRST = 5652.007595 , 
    
    SpiceJet= 6179.278881, 
    
    Air_India = 23507.019112, 
    
    Vistara = 30396.536302

AirAsia has the best value for money


📦 Dataset Source:
Kaggle - Airlines Flights Dataset

🧾 Overview
This project analyzes and models flight booking data scraped from a popular travel website. The dataset contains flight travel details between major Indian cities. The aim is to explore the data, visualize key insights, and train ML models to predict airline ticket prices based on several features.

📊 Dataset Features
The dataset includes the following columns:

Airline: Name of the airline company (6 unique airlines)

Flight: Flight code (categorical)

Source City: Departure city (6 unique cities)

Departure Time: Categorized time bins of departure (6 time labels)

Stops: Number of stops (3 distinct values)

Arrival Time: Categorized time bins of arrival (6 time labels)

Destination City: Arrival city (6 unique cities)

Class: Travel class - Business or Economy

Duration: Total travel time (continuous feature in hours)

Days Left: Days left from booking date to travel date

Price: 🎯 Target variable (flight price in INR)

🤖 Model Training & Evaluation
Two machine learning models were trained using Scikit-learn:

Linear Regression

Random Forest Regressor

Models use key features like airline, cities, class, departure time, etc., to predict ticket prices between cities like Delhi, Mumbai, Bangalore, Kolkata, Hyderabad, and Chennai.

Model	Accuracy (R² Score)	Error Margin (₹)	Predicted Ticket Price
Random Forest Regressor	0.91	₹3676.83	₹13,506.51
Linear Regression	0.90	₹4461.07	₹7173.56

✅ Random Forest Regressor showed better accuracy and lower error margin.

📈 Data Analysis & Visualizations
Using Seaborn, several visual insights were generated (see visualizations/ folder):

Total cities analyzed: 6

Longest Flight: Air India

Most Economical Airline: AirAsia

Most Expensive Airline: Vistara

Average Price by Airline:

AirAsia = ₹4,091.07

Indigo = ₹5,324.22

GO_FIRST = ₹5,652.01

SpiceJet = ₹6,179.28

Air India = ₹23,507.02

Vistara = ₹30,396.54

💡 AirAsia offers the best value for money overall.

📂 Project Structure
Copy
Edit
├── airlines_flights_data.csv
├── model_training.ipynb
├── visualizations/
│   ├── avg_price_by_airline.png
│   ├── longest_flight_airline.png
│   └── ...
├── README.md
🚀 Future Improvements
Hyperparameter tuning

Use of XGBoost or GradientBoost

Deployment as a web app using Flask or Streamlit

Real-time flight data integration

