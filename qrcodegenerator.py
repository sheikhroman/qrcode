import qrcode
import image

qr = qrcode.QRCode(
    version=15, #15 means version of qr coder image
    box_size=10, #size of the box
    border= 5 #it is white part of the image --border
)
data="https://github.com/sheikhroman"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color = "white")
img.save('test.png')