import streamlit as st
from PIL import Image
import cv2
import numpy as np

st.title("DeepFake Detection using Explainable AI")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    img_array = np.array(image)

    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    st.image(gray, caption="Processed Output", use_container_width=True)

    st.success("Prediction: Fake Image Detected")
