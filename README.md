# **Flight Data Analysis and Price Prediction** ✈️

### **Dataset Source**
[Airlines Flights Dataset from Kaggle](https://www.kaggle.com/datasets/rohitgrewal/airlines-flights-data/data)

---

## **📌 Live Demo**
You can try the deployed Streamlit app here:  
[🚀 **Open Flight Price Predictor**](https://rezzraj-flight-data-analysis-and-prediction-ai-model-app-byg5v6.streamlit.app/)

---

## **📖 Overview**
This project analyzes and models flight booking data scraped from a popular travel website.  
The dataset contains flight travel details between major Indian cities.  
The aim is to **explore the data**, **visualize key insights**, and **train ML models to predict airline ticket prices** based on several features.

---

## **📂 Dataset Features**
| Feature | Description |
|---------|-------------|
| **Airline** | Name of the airline company *(6 unique airlines)* |
| **Flight** | Flight code *(categorical)* |
| **Source City** | Departure city *(6 unique cities)* |
| **Departure Time** | Categorized time bins of departure *(6 time labels)* |
| **Stops** | Number of stops *(3 distinct values)* |
| **Arrival Time** | Categorized time bins of arrival *(6 time labels)* |
| **Destination City** | Arrival city *(6 unique cities)* |
| **Class** | Travel class - **Business** or **Economy** |
| **Duration** | Total travel time *(hours)* |
| **Days Left** | Days left from booking to travel date |
| **Price** | **Target variable** *(flight price in INR)* |

---

## **🛠 Model Training & Evaluation**
The data is split into **80% training** and **20% testing**.  
Two models were trained using **Scikit-learn**:
- **Linear Regression**
- **Random Forest Regressor**

**Key Features Used:**
- Airline
- Source & Destination cities
- Travel class
- Departure time
- Days left before travel

---

### **📊 Model Performance**
| Model | R² Score | Error Margin (₹) | Example Predicted Price |
|-------|----------|------------------|-------------------------|
| **Random Forest Regressor** | 0.91 | ₹3676.83 | ₹13,506.51 |
| **Linear Regression** | 0.90 | ₹4461.07 | ₹7,173.56 |

✅ **Random Forest** gave better accuracy and lower error margin.

---

## **📈 Feature Importance**
A feature importance graph for the Random Forest model is available in the **`visualizations/`** folder, showing which features have the most impact on predictions.

---

## **📊 Data Analysis Insights**
Using **Seaborn**, we found:
- **Total cities analyzed:** 6
- **Longest Flight:** *Air India*
- **Most Economical Airline:** *AirAsia*
- **Most Expensive Airline:** *Vistara*

### **Average Price by Airline**
| Airline | Avg. Price (₹) |
|---------|---------------|
| **AirAsia** | ₹4,091.07 |
| **Indigo** | ₹5,324.22 |
| **GO_FIRST** | ₹5,652.01 |
| **SpiceJet** | ₹6,179.28 |
| **Air India** | ₹23,507.02 |
| **Vistara** | ₹30,396.54 |

💡 **AirAsia offers the best value for money overall.**

---

## **🚀 Running Locally**
```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py



