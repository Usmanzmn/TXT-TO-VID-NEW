from diffusers import StableDiffusionPipeline
import torch

@st.cache_resource
def load_pipe():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32
    )
    pipe = pipe.to("cpu")
    return pipe

def generate_image(pipe, prompt: str, style: str, steps: int, guidance: float):
    full_prompt = f"{prompt}, {style} style"
    result = pipe(full_prompt, num_inference_steps=steps, guidance_scale=guidance)
    return result.images[0]
