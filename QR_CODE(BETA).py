import qrcode ##Importing the QR code library
website_link = input("Enter the website link: ") #Asks user for a link/text to generate its qr

#asks user for QR dimensions
a = int(input("Enter the version of QR code(1-40): "))
b = int(input("Enter the Box size of QR code(1-5): "))
c = int(input("Enter the Border size of QR code(1-5): "))

##inputs qr dimensions
qr = qrcode.QRCode(version = a, box_size = b, border = c)

qr.add_data(website_link) ##link is added to qr code
qr.make() ##qr code is generated using .make()

##color for qr
img = qr.make_image(fill_color = "black", back_color = "white")

##save's qr
img.save('youtube_qr.png')

##print's the qr
print("QR code generated and saved as youtube_qr.png")

##THE QR IS SAVED AS youtube_qr.png
