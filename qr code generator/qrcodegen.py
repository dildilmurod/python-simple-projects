import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_image = qrcode.make("Hello people!", image_factory=factory)
svg_image.save("myqr.svg")

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=1)

qr.add_data("http://ambient-studio.uz/")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("new.png")