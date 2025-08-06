# **Flight Data Analysis and Price Prediction**

### **Dataset Source**
[Airlines Flights Dataset from Kaggle](https://www.kaggle.com/datasets/rohitgrewal/airlines-flights-data/data)

---

## **Overview**
This project analyzes and models flight booking data scraped from a popular travel website. The dataset contains flight travel details between major Indian cities.  
The aim is to **explore the data**, **visualize key insights**, and **train ML models to predict airline ticket prices** based on several features.

---

## **Dataset Features**
The dataset includes the following columns:

- **Airline:** Name of the airline company *(6 unique airlines)*
- **Flight:** Flight code *(categorical)*
- **Source City:** Departure city *(6 unique cities)*
- **Departure Time:** Categorized time bins of departure *(6 time labels)*
- **Stops:** Number of stops *(3 distinct values)*
- **Arrival Time:** Categorized time bins of arrival *(6 time labels)*
- **Destination City:** Arrival city *(6 unique cities)*
- **Class:** Travel class - **Business** or **Economy**
- **Duration:** Total travel time *(continuous feature in hours)*
- **Days Left:** Days left from booking date to travel date
- **Price:** **Target variable** *(flight price in INR)*

---

## **Model Training & Evaluation**
*(The data has been split into training and testing sets)*  

Two machine learning models were trained using **Scikit-learn**:

- **Linear Regression**
- **Random Forest Regressor**

Models use key features like **airline, cities, class, departure time, etc.**, to predict ticket prices between cities like **Delhi, Mumbai, Bangalore, Kolkata, Hyderabad, and Chennai**.

### **Model Performance**
| Model                   | Accuracy (R² Score) | Error Margin (₹) | Predicted Ticket Price |
|-------------------------|----------------------|-------------------|-------------------------|
| **Random Forest Regressor** | 0.91                 | ₹3676.83          | ₹13,506.51             |
| **Linear Regression**       | 0.90                 | ₹4461.07          | ₹7173.56               |

**Random Forest Regressor showed better accuracy and lower error margin.**
##**Also added feature importance graph for random forests model ie. which features the model is most sensitive to**

---

## **Data Analysis & Visualizations**
Using **Seaborn**, several visual insights were generated (**see `visualizations/` folder**):

- **Total cities analyzed:** 6
- **Longest Flight:** *Air India*
- **Most Economical Airline:** *AirAsia*
- **Most Expensive Airline:** *Vistara*

### **Average Price by Airline**
| Airline     | Average Price (₹) |
|-------------|-------------------|
| **AirAsia** | ₹4,091.07        |
| **Indigo**  | ₹5,324.22        |
| **GO_FIRST**| ₹5,652.01        |
| **SpiceJet**| ₹6,179.28        |
| **Air India**| ₹23,507.02      |
| **Vistara** | ₹30,396.54       |

**AirAsia offers the best value for money overall.**

---




