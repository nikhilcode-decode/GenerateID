# id_card_generator/qrcode_utils.py
import qrcode
from io import BytesIO
from PIL import Image

def generate_qr_code(data: str) -> BytesIO:
    qr = qrcode.make(data)
    img_io = BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io
