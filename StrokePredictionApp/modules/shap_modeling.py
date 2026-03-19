import streamlit as st
from PIL import Image
import os

#Title
st.title("SHAP Summary Plot")

image_path = "images/shapplot.png"

image = Image.open(image_path)
st.image(image)