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

Avg Price of each airline 
     airline         price
0    AirAsia   4091.072742
1     Indigo   5324.216303
2   GO_FIRST   5652.007595
3   SpiceJet   6179.278881
4  Air_India  23507.019112
5    Vistara  30396.536302

AirAsia has the best value for money

