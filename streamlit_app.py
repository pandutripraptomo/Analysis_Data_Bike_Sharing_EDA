import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Setel judul aplikasi
st.title("🚴‍♂️ Dashboard Analisis Penyewaan Sepeda: Menyingkap Tren dan Pola Penyewaan")

# Tambahkan deskripsi atau instruksi
st.write("""
    **Selamat datang di Dashboard Analisis Penyewaan Sepeda!**
    Dashboard ini bertujuan untuk memberikan wawasan mendalam tentang **penyewaan sepeda** berdasarkan beberapa faktor utama seperti **musim**, **cuaca**, dan **waktu**.
    Dataset yang digunakan mencakup informasi terkait penyewaan sepeda oleh dua kelompok utama, yakni **pengguna casual** dan **pengguna terdaftar**.
    Mari kita jelajahi lebih jauh data dan temukan pola menarik yang tersembunyi!
""")

# Memuat data (Pastikan path file dataset sudah benar)
hour_data = pd.read_csv('hour.csv')  # Perbarui path sesuai dengan lokasi file

# Menampilkan data jika checkbox dipilih
if st.checkbox('Tampilkan Data Mentah'):
    st.subheader('Data Penyewaan Sepeda')
    st.write(hour_data.head())  # Tampilkan 5 baris pertama untuk preview data

# Visualisasi jumlah penyewaan sepeda berdasarkan musim dan cuaca
st.subheader("Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
st.write("""
    Dalam analisis ini, kita melihat bagaimana **musim** dan **kondisi cuaca** memengaruhi jumlah penyewaan sepeda.
    Visualisasi berikut memperlihatkan bagaimana **musim** (musim semi, panas, gugur, dan dingin) berhubungan dengan kondisi cuaca yang berbeda (seperti cuaca cerah, mendung, atau hujan).
""")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=hour_data, x='season', hue='weathersit', ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.set_title('Penyewaan Sepeda Berdasarkan Musim dan Cuaca')
st.pyplot(fig)

# Visualisasi jumlah penyewaan sepeda berdasarkan kondisi cuaca
st.subheader('Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
st.write("""
    Pada grafik berikut, kita dapat melihat distribusi penyewaan sepeda berdasarkan kondisi cuaca.
    **Boxplot** ini akan menunjukkan variasi jumlah penyewaan sepeda untuk setiap kategori cuaca, memberikan wawasan lebih mendalam tentang tren dan pola yang ada.
""")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=hour_data, x='weathersit', y='cnt', ax=ax2)
ax2.set_xlabel('Kondisi Cuaca')
ax2.set_ylabel('Jumlah Penyewaan Sepeda')
ax2.set_title('Distribusi Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
st.pyplot(fig2)

# Tambahkan slider untuk memilih tahun dan menampilkan data yang difilter
tahun = st.slider('Pilih Tahun', 2011, 2012, 2011)
filtered_data = hour_data[hour_data['yr'] == (tahun - 2011)]

st.write(f"Menampilkan data untuk tahun {tahun}")
st.write(filtered_data.head())  # Tampilkan 5 baris data yang difilter

# Analisis lebih dalam dengan regresi linier (Opsional)
st.write("""
    Selain visualisasi, kita juga dapat mengembangkan model prediksi untuk **menilai pengaruh fitur-fitur tertentu** terhadap jumlah penyewaan sepeda.
    Dengan menggunakan regresi linier, kita akan memprediksi jumlah penyewaan sepeda berdasarkan beberapa fitur penting seperti suhu, kelembaban, kecepatan angin, musim, dan status liburan.
""")

# Menyiapkan fitur dan target untuk prediksi
X = hour_data[['temp', 'hum', 'windspeed', 'season', 'holiday']]
y = hour_data['cnt']

# Memisahkan data untuk pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Melatih model regresi
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi dan evaluasi model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

st.write(f"**Mean Squared Error (MSE): {mse:.2f}**")
st.write("""
    **MSE (Mean Squared Error)** mengukur seberapa baik model dalam memprediksi jumlah penyewaan sepeda. 
    Nilai MSE yang lebih rendah menunjukkan model yang lebih baik dalam memprediksi hasil yang sebenarnya. 
    Dengan MSE sebesar **23359.87**, model ini memberikan gambaran yang cukup baik, meskipun masih ada ruang untuk perbaikan.
""")

# Menampilkan kesimpulan dan insight lebih lanjut
st.write("""
    Secara keseluruhan, analisis ini menunjukkan bahwa **musim** dan **cuaca** memiliki pengaruh yang signifikan terhadap jumlah penyewaan sepeda. 
    **Musim panas** dan cuaca cerah sering kali menyebabkan peningkatan penyewaan sepeda, sementara cuaca buruk seperti hujan dapat mengurangi minat penyewaan sepeda.
    
    Melalui prediksi model regresi, kita dapat memahami lebih dalam mengenai faktor-faktor yang memengaruhi jumlah penyewaan sepeda dan dapat memanfaatkan wawasan ini untuk **merencanakan kebijakan operasional** atau **strategi pemasaran** yang lebih baik.
""")
