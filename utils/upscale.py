from PIL import Image

def upscale_image(image, target_width=720):
    w, h = image.size
    scale = target_width / w
    new_size = (target_width, int(h * scale))
    return image.resize(new_size, Image.BICUBIC)
