# Encoding Data into Quick Response Code (QR Code)
import qrcode

data = input("Enter the data:")

version = int(input("Enter the version (complexity):"))     #maxvalue = 15
box_size = int(input("Enter the Box size:"))        #maxvalue = 10

qr = qrcode.QRCode(version, box_size, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

f = input("Name it as:")

img.save(f'{f}.png')

print("QR Code generated and saved in the gallery")


'''
Output:
Enter the data:www.youtube.com
Enter the version (complexity):15
Enter the Box size:2
Name it as:Youtube
QR Code generated and saved in the gallery
'''