import qrcode as qr
from PIL import Image
qrc=qr.QRCode(version=1,
              error_correction=qr.constants.ERROR_CORRECT_H,
              box_size=10,border=4)
qrc.add_data("Advance qrcode")
qrc.make(fit=True)
img=qrc.make_image(fill_color="red",back_color="blue")
img.save("Qr2.png")
