import qrcode

input_URL = input("Enter URL: ")

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 5,
    border = 1,
)

qr.add_data(input_URL)
qr.make(fit = False)

img = qr.make_image(fill_color = "black", back_color = "white")
img.save("qrcode.png")

print(qr.data_list)
