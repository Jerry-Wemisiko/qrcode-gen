from pathlib import Path


def save_qr_code_image(image, filename, output_dir="output"):
    """
    funcn to save qr code image to a DIRECTORY
    output_dir="output" creates a directory named output
    """
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    full_path = f"{output_dir}/{filename}.png"
    image.save(full_path)
    
    return full_path
