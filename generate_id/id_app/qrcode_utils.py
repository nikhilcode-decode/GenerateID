# id_app/qrcode_utils.py
import qrcode
import io
from PIL import Image
import base64

def generate_qr_code(driver_data):
    # Create QR code with driver data (name, aadhar, license, truck number)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(driver_data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a bytes buffer
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Encode the image to base64
    qr_code_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
    return qr_code_base64

