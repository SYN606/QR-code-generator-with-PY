# create a function that collects a text and converts into QR code
# save it as a picture 

import qrcode

def generate_QRcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(img_name + ".png")


data = input("Enter a link or string that want to generate as QR code :- ")
img_name = input("Name of image :- ")

generate_QRcode(data)