import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Proses data dan fungsi pembuatan dataframe tetap sama seperti sebelumnya

all_df = pd.read_csv("https://raw.githubusercontent.com/pandutripraptomo/Analysis_Data_Bike_Sharing_EDA/refs/heads/main/main_data.csv")

datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    st.image("https://raw.githubusercontent.com/pandutripraptomo/Analysis_Data_Bike_Sharing_EDA/logo.jpg")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

byhour_df = create_byhour_df(main_df)
daily_rentals_df = create_daily_rentals_df(main_df)
monthly_rentals_df = create_monthly_rentals_df(main_df)
byhour_df = create_byhour_df(main_df)
byseason_df = create_byseasons_df(main_df)
byweather_df = create_byweather_df(main_df)
clustering = create_clustering(main_df)

st.header('Pandu Tri Praptomo - Bike Sharing Dashboard 🚲')

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

st.subheader('Monthly Rentals')
fig, ax = plt.subplots(figsize=(16, 8))

# Mengubah line chart menjadi bar chart
ax.bar(
    monthly_rentals_df["dteday"],
    monthly_rentals_df["total_customer"],
    color="skyblue"
)
ax.set_xlabel("Month", fontsize=15)
ax.set_ylabel("Total Customers", fontsize=15)
ax.set_title("Monthly Rentals (Total Customers)", fontsize=20)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
ax.grid(True)

st.pyplot(fig)

season_colors = {
    'Winter': 'lightskyblue',
    'Spring': 'lightgreen',
    'Summer': 'gold',
    'Fall': 'lightcoral'
}

weather_colors = {
    'Clear':'gold', 
    'Cloudy':'lightskyblue', 
    'Light Snow/Rain':'grey', 
    'Heavy Rain/Ice Pallets':'darkblue'
}

st.subheader("Rental Patterns")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(30,15))
    # Mengganti bar chart menjadi stacked bar chart
    sns.barplot(
        y='total_customer', 
        x='season',
        data=byseason_df.sort_values(by='total_customer', ascending=False),
        palette=season_colors,
        ax=ax
    )
    ax.set_title("Customer based on Season", loc="center", fontsize=50, pad=20)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(30,15))
    # Mengganti bar chart menjadi pie chart
    sns.barplot(
        y='total_customer', 
        x='weathersit',
        data=byweather_df.sort_values(by='total_customer', ascending=False),
        palette=weather_colors,
        ax=ax
    )
    ax.set_title("Customer based on Weather", loc="center", fontsize=50, pad=20)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

st.subheader("Customer based on Hour")

# Mengganti bar chart menjadi pie chart untuk peminjaman berdasarkan jam
plt.figure(figsize=(10, 6))
byhour_df.plot(kind='pie', y='total_customer', legend=False, autopct='%1.1f%%', colors=['skyblue'], wedgeprops={'edgecolor': 'black'})
plt.title('Total Bike Rentals by Hour of the Day')
plt.ylabel('')

st.pyplot(plt)

st.subheader ("Customer Clustering by Day and Hour")

# Mengganti heatmap menjadi line plot
plt.figure(figsize=(12, 8))
sns.lineplot(data=clustering, palette="YlGnBu", dashes=False)
plt.title('Bike Rentals Line Plot by Weekday and Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')

st.pyplot(plt)

st.subheader('Registered Customer and Casual Customers')

fig, ax = plt.subplots(figsize=(16, 8))
# Mengganti line chart menjadi scatter plot
ax.scatter(
    monthly_rentals_df["dteday"],
    monthly_rentals_df["total_registered"], 
    label='Registered Rentals', color="blue", alpha=0.7)
ax.scatter(
    monthly_rentals_df["dteday"], 
    monthly_rentals_df["total_casual"], 
    label='Casual Rentals', color="gold", alpha=0.7)

ax.set_xlabel("Month")
ax.set_ylabel("Total Customers")
ax.set_title("Monthly Bike Rentals of Registered and Casual Customers")
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
ax.legend(fontsize=12)
ax.grid(True)

st.pyplot(fig)

typecust_colors = ['skyblue', 'gold']

fig, ax = plt.subplots(figsize=(14,8))
total_registered = daily_rentals_df['total_registered'].sum()
total_casual = daily_rentals_df['total_casual'].sum()
labels = ['Registered', 'Casual']
sizes = [total_registered, total_casual]
colors_typecust = ['skyblue', 'gold']

# Mengganti pie chart dengan donut chart
ax.pie(sizes, labels=labels, colors=typecust_colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85, textprops={'fontsize': 14})
ax.axis('equal')
plt.tight_layout() 
ax.set_title("Percentage of Registered vs Casual Customer", fontsize=20 , pad=20)
st.pyplot(fig) 

st.caption('Copyright © Pandu Tri Praptomo 2025')
