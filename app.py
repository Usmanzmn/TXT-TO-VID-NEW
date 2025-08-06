import sys
print("Python path:", sys.path)
import streamlit as st
import os
import uuid
from utils.image_gen import load_pipeline, generate_image
from utils.overlay import overlay_text
from utils.video_gen import make_video

st.title("🧠 Text-to-Video Generator (Streamlit + Diffusers)")

text_input = st.text_area("Enter your story or script here:")

if st.button("Generate Video"):
    with st.spinner("Loading pipeline..."):
        pipe = load_pipeline()

    os.makedirs("outputs", exist_ok=True)
    chunks = text_input.strip().split(".")
    image_paths = []

    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            continue

        prompt = chunk.strip()
        base_name = str(uuid.uuid4())
        raw_img_path = f"outputs/{base_name}_raw.png"
        final_img_path = f"outputs/{base_name}_text.png"

        st.write(f"Generating image for: *{prompt}*")
        generate_image(pipe, prompt, raw_img_path)
        overlay_text(raw_img_path, prompt, final_img_path)
        image_paths.append(final_img_path)

    video_path = make_video(image_paths)
    st.success("Video created!")

    st.video(video_path)
    with open(video_path, "rb") as f:
        st.download_button("Download Video", f, file_name="video.mp4")
