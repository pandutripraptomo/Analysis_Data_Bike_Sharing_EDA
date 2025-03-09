# 🚴‍♂️ **Bike Sharing Analysis Dashboard** 🚴‍♀️

Welcome to the **Bike Sharing Analysis Dashboard**, your interactive data hub for exploring bike sharing trends! Built with **Streamlit**, this dashboard provides insightful visualizations to help you understand what factors influence bike rentals. Whether you’re interested in exploring weather conditions, seasonal trends, or even predictions for future rentals, this app has it all!

---

## 📑 **Table of Contents**

1. [🌟 Overview](#overview)
2. [🛠️ Features](#features)
3. [⚙️ Requirements](#requirements)
4. [📥 Installation](#installation)
5. [🚀 Usage](#usage)
6. [📈 Modeling (Optional)](#modeling-optional)
7. [📊 Visualizations](#visualizations)
8. [☁️ Deploying to Streamlit Cloud](#deploying-to-streamlit-cloud)
9. [📝 License](#license)

---

## 🌟 **Overview**

This **Bike Sharing Analysis Dashboard** allows you to explore bike rental data in a fun and interactive way. By visualizing key factors like **season**, **weather**, and **time of day**, users can easily identify trends and patterns in bike sharing behavior. Whether you're curious about how different seasons affect rentals or interested in predicting future trends, this app is the perfect tool to dive into the data.

---

## 🛠️ **Features**

- **👀 Data Overview**: View raw data with a simple checkbox to explore the dataset's structure and gain insights.
- **📊 Visualizations**:
  - **Countplot**: See the number of bike rentals based on the season and weather conditions.
  - **Boxplot**: Explore the distribution of rentals under various weather conditions.
- **⚡ Interactivity**:
  - **Slider**: Filter and display data for specific years (2011 or 2012) with an interactive slider.
- **📈 Modeling** (Optional):
  - **Predictions**: A Linear Regression model predicts bike rental counts based on weather conditions, season, and more.

---

## ⚙️ **Requirements**

Before you get started, make sure you have the following Python packages installed:

- **Python 3.x**
- **Streamlit**
- **Pandas**
- **Seaborn**
- **Matplotlib**
- **Scikit-learn**

To install the required packages, run:

```bash
pip install -r requirements.txt

To install the required packages, run:

```bash
pip install -r requirements.txt
```

### requirements.txt

```plaintext
streamlit
pandas
seaborn
matplotlib
scikit-learn
```

---

## 📥 **Installation**

To get this app running on your local machine, follow these simple steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/Bike_Sharing_Analysis_Dashboard.git
   ```

2. **Navigate into the project directory**:

   ```bash
   cd Bike_Sharing_Analysis_Dashboard
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 **Usage**

Running the app is simple:

1. Ensure the **dataset file (`hour.csv`)** is in the correct path and update the file path if needed.
2. To start the Streamlit app, use the following command:

   ```bash
   streamlit run streamlit_app.py
   ```

   This will launch the app in your web browser where you can interact with it!

---

## 📈 **Modeling (Optional)**

For those interested in **predicting** bike rental counts based on weather, season, and other features, the app includes an **optional Linear Regression model**. The model uses the following features:
- Temperature
- Humidity
- Windspeed
- Season
- Holiday status

The app calculates the **Mean Squared Error (MSE)** to evaluate the performance of the regression model.

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Prepare features and target for prediction
X = hour_data[['temp', 'hum', 'windspeed', 'season', 'holiday']]
y = hour_data['cnt']

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
st.write(f"Mean Squared Error (MSE): {mse}")
```

---

## 📊 **Visualizations**

This dashboard includes several insightful visualizations:

- **Countplot**: Displays the number of bike rentals grouped by season and weather condition. You’ll quickly see how these factors affect bike rental behavior.

  Example:
  ```python
  sns.countplot(data=hour_data, x='season', hue='weathersit')
  ```

- **Boxplot**: Shows how bike rental distributions vary across different weather conditions. It helps identify how rentals fluctuate in different weather conditions.

  Example:
  ```python
  sns.boxplot(data=hour_data, x='weathersit', y='cnt')
  ```

- **Interactive Slider**: Filter the dataset by selecting a specific year (2011 or 2012). This is useful for comparing trends across different years.

---

## ☁️ **Deploying to Streamlit Cloud**

Want to share your app with the world? Deploy it to **Streamlit Cloud** in just a few steps:

1. **Push your project to GitHub** (if you haven't already).
2. Go to **[Streamlit Cloud](https://streamlit.io/cloud)** and log in with your **GitHub** account.
3. Click on **New App** and select the repository with your Streamlit app.
4. Streamlit will automatically deploy the app and provide a URL to share.

---

## 📝 **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

Now you're all set! Enjoy exploring bike sharing trends and visualizing data with this interactive dashboard. Feel free to customize and improve it, and don’t hesitate to reach out if you need help or have suggestions. 😄
```

