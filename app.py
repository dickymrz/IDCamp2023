import streamlit as st
st.title("Dashboard Streamlit Sederhana")
st.write("Contoh")

image_url = 'https://drive.google.com/drive/folders/1_x3bBERoy3jspSon-nmF4bcxsGofk2Ir?hl=id'

# Tampilkan gambar
st.image(image_url, caption='Visualisasi Data', use_column_width=True)
