import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def create_daily_rentals_df(df):
    daily_rentals_df = df.resample(rule='D', on='dteday').agg({
        "registered": "sum",
        "casual": "sum",
        "cnt": "sum"
    })
    daily_rentals_df = daily_rentals_df.reset_index()
    daily_rentals_df.rename(columns={
        "registered": "total_registered",
        "casual": "total_casual",
        "cnt": "total_customer"
    }, inplace=True)
    
    return daily_rentals_df

def create_monthly_rentals_df(df):
    # Ensure 'yr' and 'mnth' are string types for concatenation
    df['yr'] = df['yr'].astype(str)
    df['mnth'] = df['mnth'].astype(str)

    monthly_rentals_df = df.groupby(['yr', 'mnth'])[['cnt', 'registered', 'casual']].sum().reset_index()
    
    # Mapping for months to sort correctly
    mapping_mnth = {
        '1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June',
        '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'
    }
    monthly_rentals_df['mnth'] = monthly_rentals_df['mnth'].map(mapping_mnth)

    monthly_rentals_df['date'] = monthly_rentals_df['yr'] + '-' + monthly_rentals_df['mnth']
    monthly_rentals_df['date'] = pd.to_datetime(monthly_rentals_df['date'], format='%Y-%B')
    monthly_rentals_df = monthly_rentals_df.sort_values('date').reset_index(drop=True)

    monthly_rentals_df.rename(columns={
        "registered": "total_registered",
        "casual": "total_casual",
        "cnt": "total_customer"
    }, inplace=True)
    
    return monthly_rentals_df

def create_byhour_df(df):
    byhour_df = df.groupby(by="hr").cnt.sum().reset_index()
    byhour_df.rename(columns={
        "cnt": "total_customer"
    }, inplace=True)

    return byhour_df

def create_byseasons_df(df):
    # Map season numbers to names as done in the notebook for consistent display
    mapping_season = {1:'Spring', 2: 'Summer', 3:'Fall', 4:'Winter'}
    df['season'] = df['season'].map(mapping_season)
    byseason_df = df.groupby(by="season").cnt.sum().reset_index()
    byseason_df.rename(columns={
        "cnt": "total_customer"
    }, inplace=True)
    
    # Order seasons as they appear in the notebook's bar chart for consistency (Fall, Summer, Winter, Spring)
    # The order in the notebook's bar chart is from highest to lowest total rentals.
    # We'll use the sorted_values from the notebook's bar chart which implicitly uses the aggregate order.
    # The initial `sort_values(ascending=False)` will take care of this.
    byseason_df = byseason_df.sort_values(by='total_customer', ascending=False)
    
    return byseason_df

def create_byweather_df(df):
    # Map weather numbers to names as done in the notebook for consistent display
    mapping_weathersit = {1:'Clear', 2: 'Cloudy', 3:'Light Snow/Rain', 4:'Heavy Rain/Ice Pallets'}
    df['weathersit'] = df['weathersit'].map(mapping_weathersit)
    byweather_df = df.groupby(by="weathersit").cnt.sum().reset_index()
    byweather_df.rename(columns={
        "cnt": "total_customer"
    }, inplace=True)
    
    # Order weather conditions as they appear in the notebook's bar chart for consistency
    byweather_df = byweather_df.sort_values(by='total_customer', ascending=False)
    
    return byweather_df

def create_clustering(df):
    # Ensure weekday column is correctly mapped before grouping for consistent indexing with the notebook's heatmap
    # In the notebook, `main_df['weekday'] = main_df['dteday'].dt.day_name()` is used.
    # Need to make sure the weekday names match for consistency in the heatmap.
    df['weekday'] = df['dteday'].dt.day_name()
    # Ensure consistent order of weekdays for the heatmap
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    clustering = df.groupby(['weekday', 'hr'])['cnt'].sum().unstack().reindex(weekday_order)
    
    return clustering

# Load data
# The original notebook reads from /content/day.csv and /content/hour.csv,
# then processes them into 'main_df' which is then saved to 'main_data.csv'.
# The streamlit app directly loads 'main_data.csv' from GitHub.
# For consistent mapping, we should ensure the 'main_data.csv' used here has the mappings
# applied or apply them again as the notebook did for the final 'main_df'.
# The current 'main_data.csv' on GitHub already contains mapped 'yr', 'mnth', 'weekday', 'season', 'weathersit'.
# So, we just need to load it and ensure datetime conversion.
all_df = pd.read_csv("https://raw.githubusercontent.com/pandutripraptomo/Analysis_Data_Bike_Sharing_EDA/refs/heads/main/main_data.csv")

datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    st.image("https://raw.githubusercontent.com/pandutripraptomo/Analysis_Data_Bike_Sharing_EDA/main/Streamlit_Dashboard/bike.gif")
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

# Re-create DFs with selected date range.
# Pass a copy to functions that modify the DataFrame (e.g., mapping season/weather/weekday)
# to avoid modifying the original `main_df` for subsequent function calls.
daily_rentals_df = create_daily_rentals_df(main_df.copy())
monthly_rentals_df = create_monthly_rentals_df(main_df.copy())
byhour_df = create_byhour_df(main_df.copy())
byseason_df = create_byseasons_df(main_df.copy())
byweather_df = create_byweather_df(main_df.copy())
clustering = create_clustering(main_df.copy())


st.header('Pandu Tri Praptomo - Bike Sharing Dashboard 🚲')

# Daily Rentals (Metrics) - Consistent placement, good as an overview
st.subheader('Daily Rentals')

col1, col2, col3 = st.columns(3)

with col1:
    total_rentals = daily_rentals_df.total_customer.sum()
    st.metric("Total Rentals", value=total_rentals)

with col2:
    total_registered = daily_rentals_df.total_registered.sum()
    st.metric("Total Registered Customer", value=total_registered)

with col3:
    total_casual = daily_rentals_df.total_casual.sum()
    st.metric("Total Casual Customer", value=total_casual)

# --- Business Question 1: Bagaimana tren peminjaman sepeda dari tahun 2011 hingga 2012? ---
st.subheader('Monthly Bike Rentals Over Two Years') # Title adjustment
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_rentals_df["date"], # Use 'date' column
    monthly_rentals_df["total_customer"],
    marker='o', 
    linewidth=2,
    color="skyblue"
)
ax.set_xlabel("Date", fontsize=15) # Label adjustment
ax.set_ylabel("Number of Rentals", fontsize=15) # Label adjustment
ax.set_title("Monthly Bike Rentals Over Two Years", fontsize=20) # Title adjustment
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12, rotation=45) # Rotation adjustment
ax.grid(True)

st.pyplot(fig)

# --- Business Question 2: Apa saja faktor dan kondisi yang mempengaruhi total peminjaman sepeda tertinggi selama dua tahun tersebut? ---
st.subheader("Rental Patterns by Season and Weather") # New subheader for Q2 related plots

col1, col2 = st.columns(2)

season_colors = {
    'Fall': 'lightcoral', # Re-ordered based on notebook's bar chart values (highest first)
    'Summer': 'gold',
    'Winter': 'lightskyblue',
    'Spring': 'lightgreen'
}

weather_colors = {
    'Clear':'gold', 
    'Cloudy':'lightskyblue', 
    'Light Snow/Rain':'grey', 
    'Heavy Rain/Ice Pallets':'darkblue'
}

with col1:
    fig, ax = plt.subplots(figsize=(10, 6)) # Adjusted figsize to better fit column
    sns.barplot(
        y='total_customer', 
        x='season',
        data=byseason_df, # Data is already sorted by the create_byseasons_df function
        palette=season_colors, # Colors are set based on sorted order in the function
        ax=ax
    )
    ax.set_title("Total Bike Rentals by Season", loc="center", fontsize=16) # Title adjustment
    ax.set_ylabel("Total Rentals", fontsize=12) # Label adjustment
    ax.set_xlabel("Season", fontsize=12) # Label adjustment
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(10, 6)) # Adjusted figsize to better fit column
    sns.barplot(
        y='total_customer', 
        x='weathersit',
        data=byweather_df, # Data is already sorted by the create_byweather_df function
        palette=weather_colors, # Colors are set based on sorted order in the function
        ax=ax
    )
    ax.set_title("Total Bike Rentals by Weather", loc="center", fontsize=16) # Title adjustment
    ax.set_ylabel("Total Rentals", fontsize=12) # Label adjustment
    ax.set_xlabel("Weather", fontsize=12) # Label adjustment
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    st.pyplot(fig)

# Customer based on Hour (Bar Plot - Changed from Pie Chart)
st.subheader("Total Bike Rentals by Hour of the Day") # Title adjustment
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    y='total_customer', 
    x='hr',
    data=byhour_df, # Data is already sorted by hour
    color='skyblue',
    ax=ax
)
ax.set_title("Total Bike Rentals by Hour of the Day", loc="center", fontsize=16)
ax.set_xlabel('Hour', fontsize=12)
ax.set_ylabel('Total Rentals', fontsize=12)
ax.tick_params(axis='x', labelsize=10, rotation=0)
ax.tick_params(axis='y', labelsize=10)
ax.grid(axis='y') # Add y-grid as in notebook
st.pyplot(fig)

# Customer Clustering by Day and Hour (Heatmap - Changed from Line Plot)
st.subheader ("Bike Rentals Heatmap by Weekday and Hour") # Title adjustment
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(clustering, cmap="YlGnBu", annot=False, fmt=".0f", ax=ax) # Changed to heatmap
ax.set_title('Bike Rentals Heatmap by Weekday and Hour', fontsize=16) # Title adjustment
ax.set_xlabel('Hour of the Day', fontsize=12)
ax.set_ylabel('Day of the Week', fontsize=12)
st.pyplot(fig)

# --- Business Question 3: Berapa proporsi antara peminjam sepeda yang terdaftar sebagai pelanggan dan yang bukan pelanggan? ---
st.subheader('Registered Customer and Casual Customers')

# Monthly Bike Rentals of Registered and Casual Customers (Line Plot - Changed from Scatter)
fig, ax = plt.subplots(figsize=(16, 8))

ax.plot( # Changed to plot
    monthly_rentals_df["date"],
    monthly_rentals_df["total_registered"], 
    marker='o', # Added marker for consistency
    label='Registered Rentals', color="blue", alpha=0.7)
ax.plot( # Changed to plot
    monthly_rentals_df["date"], 
    monthly_rentals_df["total_casual"], 
    marker='o', # Added marker for consistency
    label='Casual Rentals', color="gold", alpha=0.7)

ax.set_xlabel("Month")
ax.set_ylabel("Total Customers")
ax.set_title("Monthly Bike Rentals of Registered and Casual Customers")
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12, rotation=45) # Rotation adjustment
ax.legend(fontsize=12)
ax.grid(True)

st.pyplot(fig)

# Percentage of Registered vs Casual Customer (Pie Chart)
typecust_colors = ['skyblue', 'gold'] # Ensure consistent colors

fig, ax = plt.subplots(figsize=(8,6)) # Adjusted figsize for better visual
total_registered = daily_rentals_df['total_registered'].sum()
total_casual = daily_rentals_df['total_casual'].sum()
labels = ['Registered', 'Casual']
sizes = [total_registered, total_casual]
colors_typecust = ['skyblue', 'gold'] # Local variable for pie chart colors

ax.pie(sizes, labels=labels, colors=colors_typecust, autopct='%1.1f%%', startangle=140, pctdistance=0.85, textprops={'fontsize': 14})
ax.axis('equal')
plt.tight_layout() 
ax.set_title("Percentage of Registered vs Casual Customer", fontsize=20 , pad=20)
st.pyplot(fig) 

st.caption('Copyright © Pandu Tri Praptomo 2025')
