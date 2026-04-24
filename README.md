# Proyek Analisis Data: E-Commerce Public Dataset 🛍️

Halo! Proyek ini merupakan submission untuk kelas **Belajar Analisis Data dengan Python** di Dicoding. Fokus utama dari analisis ini adalah membedah performa pendapatan kategori produk sepanjang tahun 2018 serta menganalisis dampak keterlambatan pengiriman terhadap kepuasan pelanggan.

Hasil analisis ini divisualisasikan dalam bentuk dashboard interaktif menggunakan **Streamlit**.

## Struktur Direktori
```text
submission/
├── dashboard/
│   ├── main_data.csv           # Dataset yang sudah dibersihkan untuk dashboard
│   └── dashboard.py            # Script utama dashboard Streamlit
├── data/
│   ├── orders_dataset.csv      # Dataset pesanan (mentah)
│   ├── order_items_dataset.csv # Dataset item pesanan (mentah)
│   └── ...                     # (File dataset mentah lainnya)
├── notebook.ipynb              # File analisis data lengkap (Wrangling, EDA, Visualisasi)
├── README.md                   # Dokumentasi proyek
├── requirements.txt            # Daftar library yang dibutuhkan
└── url.txt                     # Link dashboard Streamlit Cloud
Library yang Digunakan
Proyek ini dikembangkan dengan beberapa library utama:

Pandas: Manipulasi, pembersihan, dan agregasi data.

Matplotlib & Seaborn: Pembuatan grafik visualisasi data yang informatif.

Streamlit: Membangun antarmuka dashboard yang interaktif dan berbasis web.

Cara Menjalankan Project
1. Menjalankan Notebook (Analisis Data)
Jika kamu ingin melihat proses analisis dari awal (Data Wrangling, Cleaning, hingga EDA), silakan buka file notebook.ipynb. Kamu bisa menjalankannya di Jupyter Notebook, Google Colab, atau melalui ekstensi Jupyter di VS Code.

2. Menjalankan Dashboard di Lokal (Local Machine)
Untuk melihat dashboard secara interaktif di komputer kamu:

Persiapan: Pastikan Python sudah terinstal.

Install Dependencies: Buka terminal dan jalankan perintah:

Bash
pip install -r requirements.txt
Jalankan Dashboard: Masuk ke direktori utama proyek, lalu ketik:

Bash
streamlit run dashboard/dashboard.py
Dashboard akan otomatis terbuka di browser favoritmu!

Dashboard Cloud Deployment
Kamu juga bisa langsung melihat dashboard yang sudah aktif secara publik tanpa perlu menginstal apa pun melalui tautan berikut:
👉 https://cendikia-ecommerce-analysis.streamlit.app/

Dibuat oleh:

Nama: Cendikia Permata Dewanti

Email: cendikiapermata@gmail.com

ID Dicoding: CDCC297D6X1787

Institusi: Universitas Pembangunan Nasional "Veteran" Yogyakarta