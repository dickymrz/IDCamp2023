import streamlit as st
st.title("Dashboard Streamlit Sederhana")
st.write("Contoh")

image_url = 'https://github.com/dickymrz/IDCamp2023/blob/main/images/Top%2010%20Kategori%20Produk%20dengan%20Jumlah%20Ulasan%20Positif%20Tertinggi.png'

# Tampilkan gambar
st.image(image_url, caption='Visualisasi Data', use_column_width=True)
