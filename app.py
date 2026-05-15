import streamlit as st

st.title("DeepFake Detection using Explainable AI")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.success("Image uploaded successfully!")
