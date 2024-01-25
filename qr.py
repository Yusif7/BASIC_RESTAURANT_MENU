import qrcode

image = qrcode.make("https://fethiyedone.com")
image.save("qr.png")
