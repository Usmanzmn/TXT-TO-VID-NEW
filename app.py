import streamlit as st
from utils.image_gen import load_pipe, generate
from utils.upscale import upscale_image
import os

st.title("PixelGenius‑style AI Image Generator")
prompt = st.text_area("Enter prompt here")
style = st.selectbox("Style", ["Realistic", "Cartoon", "3D"])
steps = st.slider("Inference steps", 10, 50, 25)
guidance = st.slider("Guidance scale", 1.0, 20.0, 7.5)

if st.button("Generate"):
    pipe = load_pipe()
    img = generate(pipe, prompt, style, steps, guidance)
    out = upscale_image(img)
    st.image(out, use_column_width=True)
    with open(out, "rb") as f:
        st.download_button("Download", f, file_name="ai_image.png")
