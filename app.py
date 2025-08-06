import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
import uuid
import os
from PIL import Image

# Set up output folder
os.makedirs("outputs", exist_ok=True)

# Load pipeline (cached after first run)
@st.cache_resource
def load_pipe():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32
    )
    pipe = pipe.to("cpu")  # Change to "cuda" if using GPU
    return pipe

pipe = load_pipe()

# Streamlit UI
st.title("🖼️ Text-to-Image Generator")
prompt = st.text_area("Enter your prompt:")

if st.button("Generate Image") and prompt.strip():
    with st.spinner("Generating image..."):
        image = pipe(prompt).images[0]
        image_id = str(uuid.uuid4())
        output_path = f"outputs/{image_id}.png"
        image.save(output_path)
        st.image(image, caption="Generated Image", use_column_width=True)
        with open(output_path, "rb") as f:
            st.download_button("Download Image", f, file_name="generated.png")
