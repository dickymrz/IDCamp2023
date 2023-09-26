import streamlit as st

# Judul dashboard
st.title("Dashboard Analysist Data E-Commerce Public")

# Deskripsi
st.write("Berikut adalah visualisasi data yang mencakup berbagai aspek Data E-Commerce Public.")

# Container untuk gambar dan deskripsi
with st.beta_container():
    # Gambar 1
    image_path = "images/Top 10 Kota dengan Jumlah Pemesanan Tertinggi.png"
    st.image(image_path, caption="Top 10 Kota dengan Jumlah Pemesanan Tertinggi", use_column_width=True)
    
    # Deskripsi Gambar 1
    st.write("Gambar ini menunjukkan daftar 10 kota dengan jumlah pemesanan tertinggi.")

with st.beta_container():
    # Gambar 2
    image_path = "images/Top 10 Kategori Produk dengan Jumlah Ulasan Positif Tertinggi.png"
    st.image(image_path, caption="Top 10 Kategori Produk dengan Jumlah Ulasan Positif Tertinggi", use_column_width=True)
    
    # Deskripsi Gambar 2
    st.write("Gambar ini menunjukkan daftar 10 kategori produk dengan jumlah ulasan positif tertinggi.")

with st.beta_container():
    # Gambar 3
    image_path = "images/Produk dengan Jumlah Penjualan Tertinggi dan Terendah.png"
    st.image(image_path, caption="Produk dengan Jumlah Penjualan Tertinggi dan Terendah", use_column_width=True)
    
    # Deskripsi Gambar 3
    st.write("Gambar ini membandingkan produk dengan jumlah penjualan tertinggi dan terendah.")

with st.beta_container():
    # Gambar 4
    image_path = "images/Produk dengan Harga Tertinggi dan Terendah.png"
    st.image(image_path, caption="Produk dengan Harga Tertinggi dan Terendah", use_column_width=True)
    
    # Deskripsi Gambar 4
    st.write("Gambar ini menampilkan produk dengan harga tertinggi dan terendah dalam kategori tertentu.")

with st.beta_container():
    # Gambar 5
    image_path = "images/Total Pendapatan Penjualan Perusahaan.png"
    st.image(image_path, caption="Total Pendapatan Penjualan Perusahaan", use_column_width=True)
    
    # Deskripsi Gambar 5
    st.write("Gambar ini menunjukkan total pendapatan penjualan perusahaan.")
