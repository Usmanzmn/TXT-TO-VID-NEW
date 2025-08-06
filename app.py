import streamlit as st
from utils.image_gen import load_pipe, generate_image
from utils.upscale import upscale_image
import uuid
import os

st.title("🖼️ PixelGenius‑style AI Image Generator")
prompt = st.text_area("Enter your prompt")
style = st.selectbox("Style", ["Realistic", "Cartoon", "3D"])
steps = st.slider("Inference Steps", min_value=10, max_value=50, value=25)
guidance = st.slider("Guidance Scale", min_value=1.0, max_value=20.0, value=7.5)

if st.button("Generate"):
    pipe = load_pipe()
    with st.spinner("Generating image..."):
        img = generate_image(pipe, prompt, style, steps, guidance)
    out_img = upscale_image(img)

    st.image(out_img, caption="Generated Image", use_column_width=True)
    img_id = str(uuid.uuid4())
    local_path = f"outputs/{img_id}.png"
    out_img.save(local_path)

    with open(local_path, "rb") as f:
        st.download_button("Download Image", f, file_name="ai_image.png")
