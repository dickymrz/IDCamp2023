import streamlit as st

# Judul dashboard
st.title("E-Commerce Public Data Analysis Dashboard")

# Gambar 1
image_path = "images/Top 10 Kota dengan Jumlah Pemesanan Tertinggi.png"
st.image(image_path, caption="Gambar ini menunjukkan daftar 10 kota dengan jumlah pemesanan tertinggi", use_column_width=True)

# Deskripsi Gambar 1
st.write("Kota yang paling sering melakukan pemesanan produk adalah **Rio de Janeiro**")

# Gambar 2
image_path = "images/Top 10 Kategori Produk dengan Jumlah Ulasan Positif Tertinggi.png"
st.image(image_path, caption="Gambar ini menunjukkan daftar 10 kategori produk dengan jumlah ulasan positif tertinggi", use_column_width=True)

# Deskripsi Gambar 2
st.write("Persentase produk yang menerima ulasan positif sebesar **75.56%**.")
st.write("Selain itu, kategori produk dengan jumlah ulasan positif tertinggi adalah **Moveis Decoracao**")

# Gambar 3
image_path = "images/Produk dengan Jumlah Penjualan Tertinggi dan Terendah.png"
st.image(image_path, caption="Gambar ini membandingkan produk dengan jumlah penjualan tertinggi dan terendah", use_column_width=True)

# Deskripsi Gambar 3
st.write("Produk dengan jumlah penjualan tertinggi adalah **Ferramentas Jardim** dengan total penjualan sebanyak **798 unit**.")
st.write("Di sisi lain, produk dengan jumlah penjualan terendah adalah **Perfumaria** dengan hanya **1 unit** terjual.")

# Gambar 4
image_path = "images/Produk dengan Harga Tertinggi dan Terendah.png"
st.image(image_path, caption="Gambar ini menampilkan produk dengan harga tertinggi dan terendah dalam kategori tertentu", use_column_width=True)

# Deskripsi Gambar 4
st.write("Produk dengan harga tertinggi adalah **utilidades_domesticas** dengan harga sebesar **6735.0**")
st.write("Di sisi lain, produk dengan harga terendah adalah **agro_industria_e_comercio** dengan harga sebesar **0.85**")

# Gambar 5
image_path = "images/Total Pendapatan Penjualan Perusahaan.png"
st.image(image_path, caption="Gambar ini menunjukkan total pendapatan penjualan perusahaan", use_column_width=True)

# Deskripsi Gambar 5
st.write("Total pendapatan penjualan perusahaan selama periode waktu dari 4 September 2016 hingga 17 Oktober 2018 adalah sebesar **1.669.800.762**")
