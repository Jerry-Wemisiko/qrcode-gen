from PIL import Image
import subprocess
import platform
import os

def show_qr_code(file_path):
    """
    display the QR code image using the default image viewer.
    """
    
    try:
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", file_path])
        else:
            subprocess.run(["xdg-open", file_path])
    except Exception as e:
        print(f"Couldn't display image: {e}")
        print(f"manually path :{os.path.abspath(file_path)}")
        
        