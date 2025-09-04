import qrcode
# this file makes a qrcode from a url
data = input('Enter the text or URL: ').strip() # removes the white spaces arount the text
filename = input('Enter the filename: ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print("QR code save in ", filename)