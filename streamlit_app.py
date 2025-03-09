import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setel judul aplikasi
st.title("🚴‍♂️ Dashboard Analisis Penyewaan Sepeda")

# Tambahkan deskripsi atau instruksi
st.write("""
    Dashboard ini menampilkan analisis data penyewaan sepeda berdasarkan berbagai faktor seperti musim, cuaca, dan waktu.
    Dataset ini berisi informasi tentang peminjaman sepeda, termasuk pengguna casual dan terdaftar.
""")

# Memuat data (Pastikan path file dataset sudah benar)
hour_data = pd.read_csv('/path/to/hour.csv')  # Perbarui path sesuai dengan lokasi file

# Menampilkan data jika checkbox dipilih
if st.checkbox('Tampilkan Data Mentah'):
    st.subheader('Data Penyewaan Sepeda')
    st.write(hour_data.head())

# Visualisasi jumlah penyewaan sepeda berdasarkan musim dan cuaca
st.subheader("Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=hour_data, x='season', hue='weathersit', ax=ax)
st.pyplot(fig)

# Visualisasi jumlah penyewaan sepeda berdasarkan kondisi cuaca
st.subheader('Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=hour_data, x='weathersit', y='cnt', ax=ax2)
st.pyplot(fig2)

# Tambahkan slider untuk memilih tahun dan menampilkan data yang difilter
tahun = st.slider('Pilih Tahun', 2011, 2012, 2011)
filtered_data = hour_data[hour_data['yr'] == (tahun - 2011)]

st.write(f"Menampilkan data untuk tahun {tahun}")
st.write(filtered_data.head())

# Opsional, menambahkan model regresi atau prediksi (contoh: prediksi jumlah penyewaan sepeda)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Menyiapkan fitur dan target untuk prediksi (Contoh: Suhu, kelembaban, dll.)
X = hour_data[['temp', 'hum', 'windspeed', 'season', 'holiday']]
y = hour_data['cnt']

# Memisahkan data untuk pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Melatih model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)

# Evaluasi model
mse = mean_squared_error(y_test, y_pred)
st.write(f"Mean Squared Error (MSE): {mse}")


