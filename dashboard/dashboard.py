import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="E-Commerce Analysis Dashboard", 
    page_icon="🛍️", 
    layout="wide"
)

# 1. Fungsi Load Data
@st.cache_data
def load_data():
    # Pastikan file main_data.csv sudah ada di folder dashboard
    df = pd.read_csv("dashboard/main_data.csv")
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])
    df["order_estimated_delivery_date"] = pd.to_datetime(df["order_estimated_delivery_date"])
    return df

all_df_2018 = load_data()

# ==========================================
# SIDEBAR (Filter Panel - Back to Date Input)
# ==========================================
with st.sidebar:
    # Logo/Profil
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png") 
    
    # Judul Dashboard (Centered)
    st.markdown("<h1 style='text-align: center;'>E-Commerce Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Header Filter
    st.header("Filter Panel")
    
    # --- Filter 1: Rentang Waktu (KEMBALI KE DATE INPUT) ---
    min_date = all_df_2018["order_purchase_timestamp"].min().date()
    max_date = all_df_2018["order_purchase_timestamp"].max().date()

    # Menggunakan date_input sesuai permintaan (Versi Sebelumnya)
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Filter 2: Kategori Produk (Multiselect tetap ada) ---
    category_list = sorted(all_df_2018["product_category_name_english"].unique().tolist())
    selected_categories = st.multiselect(
        label="Pilih Kategori Produk",
        options=category_list,
        default=[] # Kosong berarti menampilkan semua
    )
    
    st.markdown("---")
    
    # Profil Pembuat
    st.write("**Created by:**")
    st.write("Cendikia Permata Dewanti")
    st.write("Data Scientist Path - CDC 17")
    st.write("ID: CDCC297D6X1787")

# ==========================================
# LOGIKA FILTER DATA
# ==========================================

# 1. Filter berdasarkan tanggal
main_df = all_df_2018[
    (all_df_2018["order_purchase_timestamp"].dt.date >= start_date) & 
    (all_df_2018["order_purchase_timestamp"].dt.date <= end_date)
].copy()

# 2. Filter berdasarkan kategori
if selected_categories:
    main_df = main_df[main_df["product_category_name_english"].isin(selected_categories)]

# ==========================================
# MAIN CONTENT
# ==========================================
st.title("E-Commerce Public Dataset Analysis 🛍️")
st.markdown(f"Menampilkan ringkasan data dari **{start_date}** sampai **{end_date}**")

# Row 1: Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Orders", value=main_df.order_id.nunique())
with col2:
    st.metric("Total Revenue", value=f"BRL {main_df.price.sum():,.2f}")
with col3:
    st.metric("Avg. Review Score", value=f"{main_df.review_score.mean():.2f} / 5")

st.divider()

# --- VISUALISASI 1: Performa Kategori Produk ---
st.subheader("1. Product Category Revenue Performance")
category_revenue = main_df.groupby("product_category_name_english").price.sum().sort_values(ascending=False).reset_index()

fig1, ax1 = plt.subplots(nrows=1, ncols=2, figsize=(24, 10))
colors_top = ["#2E86AB"] + ["#D3D3D3"] * 4
colors_bottom = ["#D90429"] + ["#D3D3D3"] * 4

# Top 5
sns.barplot(x="price", y="product_category_name_english", data=category_revenue.head(5), palette=colors_top, ax=ax1[0], hue="product_category_name_english", legend=False)
ax1[0].set_title("5 Kategori Pendapatan Tertinggi", fontsize=25)
ax1[0].set_ylabel(None)

# Bottom 5
sns.barplot(x="price", y="product_category_name_english", data=category_revenue.tail(5).sort_values(by='price'), palette=colors_bottom, ax=ax1[1], hue="product_category_name_english", legend=False)
ax1[1].set_title("5 Kategori Pendapatan Terendah", fontsize=25)
ax1[1].invert_xaxis()
ax1[1].yaxis.tick_right()
ax1[1].set_ylabel(None)

st.pyplot(fig1)

st.markdown("<br>", unsafe_allow_html=True)

# --- VISUALISASI 2: Tren Logistik & Dampak Kepuasan (DUA GRAFIK) ---
st.subheader("2. Delivery Analysis & Customer Satisfaction")

# A. Persiapan Data Keterlambatan
main_df['is_late'] = main_df['order_delivered_customer_date'] > main_df['order_estimated_delivery_date']

# Data Tren Bulanan (Line Chart)
main_df['month'] = main_df['order_purchase_timestamp'].dt.to_period('M').astype(str)
delay_trend = main_df.groupby('month')['is_late'].mean() * 100
delay_trend_df = delay_trend.reset_index()

# Data Dampak Review (Bar Chart)
review_impact = main_df.drop_duplicates(subset=['order_id']).groupby('is_late')['review_score'].mean().reset_index()
review_impact['is_late'] = review_impact['is_late'].map({False: 'On Time', True: 'Late'})

# B. Membuat Figure dengan 2 Subplot (Atas-Bawah)
fig2, ax2 = plt.subplots(nrows=2, ncols=1, figsize=(15, 18))

# PLOT ATAS: Tren Keterlambatan Bulanan (Line Chart)
sns.lineplot(
    x="month", 
    y="is_late", 
    data=delay_trend_df, 
    marker="o", 
    linewidth=3,
    markersize=8,
    color="#F4A261", 
    ax=ax2[0]
)
ax2[0].set_title("Tren Persentase Keterlambatan Pengiriman Bulanan (2018)", fontsize=22, pad=15)
ax2[0].set_ylabel("Persentase Terlambat (%)", fontsize=14)
ax2[0].set_xlabel(None)

# PLOT BAWAH: Dampak Keterlambatan terhadap Review Score (Bar Chart)
colors_review = ["#2A9D8F", "#E76F51"]
sns.barplot(
    x="is_late", 
    y="review_score", 
    data=review_impact, 
    palette=colors_review, 
    ax=ax2[1],
    hue="is_late",
    legend=False
)

# Tambahkan label angka di atas batang
for p in ax2[1].patches:
    ax2[1].annotate(format(p.get_height(), '.2f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points',
                   fontsize=14, fontweight='bold')

ax2[1].set_title("Rata-rata Review Score: On Time vs Late", fontsize=22, pad=15)
ax2[1].set_ylabel("Average Rating (1-5)", fontsize=14)
ax2[1].set_xlabel(None)
ax2[1].set_ylim(0, 5)

plt.tight_layout(pad=5.0)
st.pyplot(fig2)

# Footer
st.caption(f'Copyright (c) {datetime.now().year} | Cendikia Permata Dewanti | Data Scientist Path ')