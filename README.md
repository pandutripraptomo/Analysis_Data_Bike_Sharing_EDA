
---

# Analisis dan Dashboard Data Peminjaman Sepeda (2011-2012)

Proyek ini menganalisis performa peminjaman sepeda dari tahun 2011 hingga 2012, serta menyediakan panduan untuk menjalankan *dashboard* visualisasinya.

## Ikhtisar Performa Peminjaman Sepeda

Jumlah peminjaman sepeda menunjukkan **peningkatan signifikan setiap tahun dari kuartal 2 ke kuartal 3**, diikuti penurunan di akhir tahun.

### Kondisi Peminjaman Tertinggi

Peminjaman sepeda mencapai puncaknya pada kondisi berikut:
* **Musim Gugur** adalah musim dengan peminjaman tertinggi.
* **Cuaca cerah atau sedikit berawan** paling banyak diminati.
* **Waktu tersibuk** adalah pukul 5-6 sore dan pukul 8 pagi.
* **Hari kerja (Senin-Jumat)** menunjukkan jumlah peminjam yang lebih tinggi, sementara **Sabtu dan Minggu** ramai dari jam 12 siang hingga 3 sore.

### Profil Peminjam

* **Pelanggan terdaftar** jauh lebih banyak dibandingkan peminjam biasa.
* Meskipun jumlahnya lebih sedikit, ada **potensi besar untuk menarik peminjam baru (pengguna kasual)** melalui strategi pemasaran yang tepat.

## Kesimpulan dan Rekomendasi

Untuk meningkatkan peminjaman sepeda, fokuskan strategi pemasaran pada:
* **Menarik lebih banyak peminjam baru** yang belum terdaftar.
* **Memanfaatkan waktu dan kondisi cuaca puncak** yang telah teridentifikasi.

Dengan menerapkan rekomendasi ini, diharapkan bisnis dapat meningkatkan performa dan memperluas basis pelanggannya.

---

## Cara Menjalankan Dashboard Secara Lokal

Ikuti langkah-langkah di bawah ini untuk menginstal dependensi dan menjalankan *dashboard* di perangkat Anda.

### Instalasi Dependensi

#### Menggunakan Anaconda

```bash
conda create --name main-ds python=3.11.9
conda activate main-ds
pip install -r requirements.txt
```

#### Menggunakan Shell/Terminal Biasa

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

### Menjalankan Dashboard

Setelah instalasi selesai, jalankan perintah ini di terminal:

```bash
cd dashboard
streamlit run dashboard.py
```
