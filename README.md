# Bike Sharing Data Analysis Dashboard ✨

## Deskripsi Proyek

Proyek ini adalah aplikasi **Streamlit** yang menganalisis dan memvisualisasikan data peminjaman sepeda menggunakan dataset **Bike Sharing**. Aplikasi ini mengintegrasikan berbagai analisis data, visualisasi interaktif, dan fitur-fitur menarik untuk memudahkan pemahaman tentang pola penggunaan sepeda berdasarkan waktu, cuaca, musim, dan jenis pelanggan.

### Fitur Utama:
- **Dashboard Interaktif** yang menampilkan data peminjaman sepeda harian, bulanan, berdasarkan jam, musim, dan cuaca.
- **Grafik dan Visualisasi** menggunakan **Matplotlib**, **Seaborn**, dan **Plotly**.
- **Analisis** berdasarkan:
  - Jumlah peminjam sepeda harian dan bulanan.
  - Distribusi peminjaman berdasarkan jam, cuaca, dan musim.
  - Analisis cluster berdasarkan hari dan jam.
- **Menampilkan GIF animasi** sepeda yang menarik di sidebar untuk memperkaya pengalaman pengguna.

### Prasyarat

Sebelum menjalankan aplikasi ini, pastikan Anda memiliki **Python** yang terinstal di sistem Anda. Berikut adalah daftar pustaka yang dibutuhkan:

- **Streamlit**: Untuk membuat dashboard interaktif.
- **Pandas**: Untuk manipulasi data.
- **Matplotlib**: Untuk membuat visualisasi grafik.
- **Seaborn**: Untuk visualisasi statistik.
- **Plotly**: Untuk grafik interaktif.
- **Streamlit-folium**: Jika ingin menambahkan peta interaktif (opsional).

### Setup Environment

Pilih salah satu cara berikut untuk setup lingkungan pengembangan:

### 1. **Setup Environment - Anaconda**

Jika Anda menggunakan **Anaconda**, Anda dapat mengikuti langkah-langkah berikut untuk membuat lingkungan terpisah:

### Membuat lingkungan virtual dengan Anaconda
conda create --name main-ds python=3.9

### Mengaktifkan lingkungan
conda activate main-ds

### Install dependencies dari requirements.txt
pip install -r requirements.txt


### 2. **Setup Environment - Shell/Terminal**

Jika Anda menggunakan **pipenv**, berikut adalah langkah-langkah untuk setup proyek:


# Membuat direktori proyek
mkdir proyek_analisis_data
cd proyek_analisis_data

# Install dependencies dengan pipenv
pipenv install

# Masuk ke shell pipenv
pipenv shell

# Install dependencies dari requirements.txt
pip install -r requirements.txt


## Menjalankan Aplikasi

Setelah menyiapkan lingkungan, Anda dapat menjalankan aplikasi **Streamlit** dengan langkah-langkah berikut:


# Jalankan aplikasi Streamlit
streamlit run dashboard.py


Aplikasi ini akan terbuka di browser default Anda.

## Fitur Aplikasi

* **Data Interaktif**: Gunakan filter tanggal untuk menyesuaikan rentang waktu yang ingin Anda lihat.
* **Grafik Peminjaman Sepeda**: Menampilkan grafik bulanan dan harian mengenai peminjaman sepeda secara keseluruhan, peminjam terdaftar, dan peminjam kasual.
* **Analisis Berdasarkan Jam dan Musim**: Menampilkan tren peminjaman sepeda berdasarkan jam dalam sehari dan musim.
* **Pemetaan Interaktif**: Visualisasikan data berbasis lokasi dengan peta interaktif (jika ditambahkan).

## Struktur Proyek

Bike-Sharing-Dashboard/
├── dashboard.py            # Aplikasi Streamlit utama
├── data/
│   ├── bike_sharing.csv   # Dataset Bike Sharing
├── images/
│   └── logo.gif           # GIF atau gambar logo yang digunakan di aplikasi
└── README.md              # Dokumentasi proyek

## Penulis

* **Pandu Tri Praptomo** - [LinkedIn](https://www.linkedin.com/in/pandutripraptomo/) | [GitHub](https://github.com/pandutripraptomo)

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

## Kontak

Jika Anda memiliki pertanyaan atau ingin berkontribusi dalam pengembangan proyek ini, jangan ragu untuk menghubungi saya di **[pandutripraptomo@gmail.com](mailto:pandutripraptomo@gmail.com)**.

### Penjelasan:
1. **Deskripsi Proyek**: Menggambarkan aplikasi yang dibangun dengan tujuan analisis data peminjaman sepeda.
2. **Prasyarat**: Menyebutkan pustaka yang dibutuhkan untuk menjalankan aplikasi.
3. **Setup Environment**: Menyediakan dua opsi untuk setup lingkungan pengembangan, yaitu menggunakan Anaconda atau `pipenv` dengan instruksi yang jelas.
4. **Menjalankan Aplikasi**: Memberikan instruksi untuk menjalankan aplikasi Streamlit dengan perintah `streamlit run`.
5. **Fitur Aplikasi**: Menyediakan rincian tentang fitur utama aplikasi.
6. **Struktur Proyek**: Memberikan gambaran tentang struktur folder dan file dalam proyek.
7. **Penulis dan Lisensi**: Menyertakan informasi tentang kontributor proyek dan lisensinya.

Anda dapat menyesuaikan lebih lanjut jika ada detail atau fitur tambahan pada proyek Anda!

