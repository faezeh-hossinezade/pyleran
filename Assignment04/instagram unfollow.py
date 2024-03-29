import qrcode
img = qrcode.make('fazyhossinezade@gmail.com')
type(img)  # qrcode.image.pil.PilImage
img.save("my_first_qrcode.png")