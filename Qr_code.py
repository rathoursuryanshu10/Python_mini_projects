import qrcode as qr
create_qr=input("Enter the text/Link to create QRCode :: ")
img = qr.make(create_qr)
img.save("Qr_created.png")
