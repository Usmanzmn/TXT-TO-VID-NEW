from PIL import Image, ImageDraw, ImageFont

def overlay_text(image_path, text, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Wrap long text (optional)
    lines = text.split('\n')
    y = image.height - 100

    for line in lines:
        draw.text((20, y), line, font=font, fill="white")
        y += 20

    image.save(output_path)
    return output_path
