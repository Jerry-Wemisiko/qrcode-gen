from qrcode.qr import generate_qr_code
from qrcode.utils.utils import save_qr_code_image
from qrcode.utils.display import show_qr_code

import os

def main():
    
    print("+++ QR Code Generator +++")
    
    # Get user input
    data = input("Enter the data to be encoded in the QR code: ").strip()#REMOVES WHITESPACE
    filename = input("Enter the filename to save the QR code (without extension): ").strip()
    try:
        img = generate_qr_code(data, filename)
        saved_path = save_qr_code_image(img, filename)
        
        print(f"QR code saved to {saved_path}")
        
        if input("\nDisplay the QR code? (y/n): ").strip().lower() == 'y':
            
            show_qr_code(saved_path)
            
    except Exception as e:
            print(f"An error occurred: {e}")
                
if __name__ == "__main__":
        main()
        
            
        