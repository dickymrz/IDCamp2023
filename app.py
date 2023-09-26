import streamlit as st
from PIL import Image

image = Image.open('https://drive.google.com/file/d/19BwOzCsaf4P9lZ-Wuwtj9MXt6YjELk3n/view?usp=drive_link')

st.image(image, caption='Test')

