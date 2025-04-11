import qrcode

def generate_qr_code(data, filename, fill_color="black", backcolor="white",box_size=10):
    """"
    generate a QR code with basic customization and save it to a file.
    Parameters:data:data to be encoded in the QR code
    filename:filename to save the QR code image
    fill_color:color of the QR code
    back_color:background color of the QR code
    box_size:size of each box in the QR code
    """
    qr =qcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img =qr.make_image(fill_color=fill_color, back_color=backcolor)
    return