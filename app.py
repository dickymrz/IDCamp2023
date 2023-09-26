import streamlit as st

# Gambar 1
image_path = "images/Top 10 Kota dengan Jumlah Pemesanan Tertinggi.png"
st.image(image_path, caption="Top 10 Kota dengan Jumlah Pemesanan Tertinggi", use_column_width=True)

# Gambar 2
image_path = "images/Top 10 Kategori Produk dengan Jumlah Ulasan Positif Tertinggi.png"
st.image(image_path, caption="Top 10 Kategori Produk dengan Jumlah Ulasan Positif Tertinggi", use_column_width=True)

# Gambar 3
image_path = "images/Produk dengan Jumlah Penjualan Tertinggi dan Terendah.png"
st.image(image_path, caption="Produk dengan Jumlah Penjualan Tertinggi dan Terendah", use_column_width=True)

# Gambar 4
image_path = "images/Total Pendapatan Penjualan Perusahaan.png"
st.image(image_path, caption="Total Pendapatan Penjualan Perusahaan", use_column_width=True)

# Gambar 5
image_path = "images/Produk dengan Harga Tertinggi dan Terendah.png"
st.image(image_path, caption="Produk dengan Harga Tertinggi dan Terendah", use_column_width=True)

# Membagi layar menjadi dua kolom
left_column, right_column = st.columns(2)

# Tampilkan gambar di kolom kiri
with left_column:
    st.image("images/Produk dengan Jumlah Penjualan Tertinggi dan Terendah.png", caption="Produk dengan Jumlah Penjualan Tertinggi dan Terendah", use_column_width=True)

# Tampilkan gambar di kolom kanan
with right_column:
    st.image("images/Produk dengan Harga Tertinggi dan Terendah.png", caption="Produk dengan Harga Tertinggi dan Terendah", use_column_width=True)
