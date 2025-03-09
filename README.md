# Bike Sharing Analysis Dashboard

This project is a **Bike Sharing Analysis Dashboard** built with **Streamlit**, which provides an interactive visualization and analysis of bike sharing data. The dataset includes various factors influencing bike rentals, such as season, weather conditions, and time of day. This dashboard allows users to explore data, visualize trends, and evaluate predictive models on bike rentals.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Modeling (Optional)](#modeling-optional)
7. [Visualizations](#visualizations)
8. [Deploying to Streamlit Cloud](#deploying-to-streamlit-cloud)
9. [License](#license)

## Overview

The **Bike Sharing Analysis Dashboard** is designed to help users analyze bike rental data by providing insightful visualizations. The dashboard includes data visualization based on various factors like the weather, season, and time of day. Users can interact with the data and visualize trends over different years, and the app includes a predictive model for forecasting bike rentals based on various features.

## Features

- **Judul & Deskripsi**: Menampilkan judul dan deskripsi aplikasi.
- **Menampilkan Data**: Tampilkan data mentah dengan checkbox.
- **Visualisasi**:
  - **Countplot**: Menampilkan jumlah penyewaan sepeda berdasarkan musim dan cuaca.
  - **Boxplot**: Menampilkan distribusi penyewaan sepeda berdasarkan kondisi cuaca.
- **Elemen Interaktif**:
  - **Slider**: Untuk memfilter dan menampilkan data berdasarkan tahun yang dipilih (2011 atau 2012).
- **Pemodelan** (Opsional):
  - **Prediksi**: Regresi linear untuk memprediksi jumlah penyewaan sepeda berdasarkan fitur seperti suhu, kelembaban, dan kecepatan angin.
  
## Requirements

- **Python 3.x**
- **Streamlit**
- **Pandas**
- **Seaborn**
- **Matplotlib**
- **Scikit-learn**

You can install these dependencies by running:

```bash
pip install -r requirements.txt
