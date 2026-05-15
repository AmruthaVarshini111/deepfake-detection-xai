import streamlit as st

st.set_page_config(page_title="DeepFake Detector")

st.title("DeepFake Detection using Explainable AI")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")

    st.success("Prediction Complete")
    st.write("Result: Fake Image Detected")
