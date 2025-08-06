from moviepy.editor import ImageSequenceClip

def make_video(image_paths, output_path="outputs/final_video.mp4", fps=1):
    clip = ImageSequenceClip(image_paths, fps=fps)
    clip.write_videofile(output_path, codec="libx264")
    return output_path
