import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the title of the app
st.title("🚴‍♂️ Bike Sharing Analysis Dashboard")

# Add description or instructions
st.write("""
    This dashboard displays the analysis of bike sharing data based on various factors like season, weather, and time.
    The dataset provides information about bike rentals, including casual and registered users.
""")

# Load the data (Make sure you have uploaded the correct file path)
hour_data = pd.read_csv('/path/to/hour.csv')  # Update the path accordingly

# Display data if checkbox is selected
if st.checkbox('Show Raw Data'):
    st.subheader('Bike Sharing Data')
    st.write(hour_data.head())

# Visualize the number of bike rentals by season and weather
st.subheader("Bike Rentals by Season and Weather")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=hour_data, x='season', hue='weathersit', ax=ax)
st.pyplot(fig)

# Visualize the number of bike rentals based on weather conditions
st.subheader('Bike Rentals by Weather Conditions')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=hour_data, x='weathersit', y='cnt', ax=ax2)
st.pyplot(fig2)

# Add a slider to select the year and display filtered data
year = st.slider('Select Year', 2011, 2012, 2011)
filtered_data = hour_data[hour_data['yr'] == (year - 2011)]

st.write(f"Showing data for year {year}")
st.write(filtered_data.head())

# Optionally, add a regression model or predictions (e.g., bike rental prediction)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Prepare features and target for prediction (Example: Temperature, humidity, etc.)
X = hour_data[['temp', 'hum', 'windspeed', 'season', 'holiday']]
y = hour_data['cnt']

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
st.write(f"Mean Squared Error (MSE): {mse}")
