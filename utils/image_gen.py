from diffusers import StableDiffusionPipeline
import torch

def load_pipeline():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cpu")  # Use "cuda" if you have a GPU
    return pipe

def generate_image(pipe, prompt, output_path):
    image = pipe(prompt).images[0]
    image.save(output_path)
    return output_path
