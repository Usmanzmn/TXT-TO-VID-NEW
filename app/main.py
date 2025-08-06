import torch
from diffusers import StableDiffusionPipeline
from huggingface_hub import login
import os
from PIL import Image
import io
from utils.logger import setup_logger

logger = setup_logger()

class StableDiffusion15:
    def __init__(self):
        self.device = "cpu"
        logger.info(f"Initialized device as: {self.device}")
        logger.info(f"CUDA available: {torch.cuda.is_available()}")

        # Login using token (if available)
        hf_token = os.environ.get("HF_TOKEN")
        if hf_token:
            login(hf_token)

        self.pipe = self.load_pipeline()

    def load_pipeline(self):
        logger.info(f"Loading SD Turbo pipeline on device: {self.device}")
        pipe = StableDiffusionPipeline.from_pretrained(
            "stabilityai/sd-turbo",
            use_auth_token=os.environ.get("HF_TOKEN"),
            torch_dtype=torch.float32
        ).to(self.device)
        return pipe

    def generate_hd_image(self, prompt, steps=4, guidance_scale=1.0):
        logger.info(f"Generating image with prompt: {prompt}, steps: {steps}, guidance: {guidance_scale}")
        
        image = self.pipe(prompt=prompt, num_inference_steps=steps, guidance_scale=guidance_scale).images[0]

        return image


# Dispatcher
def generate_hd_image(prompt, model_key, steps, guidance_scale):
    model = StableDiffusion15()  # Hardcoded to sd-turbo
    return model.generate_hd_image(prompt, steps, guidance_scale)
