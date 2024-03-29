import qrcode
name_phone=input('please enter your name and phone number:')
img = qrcode.make(name_phone)
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode.png")