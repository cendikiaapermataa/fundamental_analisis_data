# Proyek Analisis Data: E-Commerce Public Dataset 🛍️

Proyek ini merupakan submission untuk kelas **Belajar Analisis Data dengan Python** di Dicoding. Fokus utama dari analisis ini adalah membedah performa pendapatan kategori produk sepanjang tahun 2018 serta menganalisis hubungan antara keterlambatan pengiriman dengan kepuasan pelanggan.

## Struktur Direktori
- `/dashboard`: Berisi file utama untuk dashboard Streamlit (`dashboard.py`) dan dataset yang sudah dibersihkan (`main_data.csv`).
- `/data`: Berisi dataset mentah (raw data) dalam format CSV.
- `notebook.ipynb`: File Jupyter Notebook yang berisi proses analisis data lengkap.
- `requirements.txt`: Daftar library Python beserta versinya.
- `url.txt`: Berisi link dashboard Streamlit Cloud.

## Setup Environment - Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit App
```bash
streamlit run dashboard/dashboard.py
```