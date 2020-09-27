#in CMD type: pip install qrcode[pil]
import qrcode

#Basic QRcode generator
qr = qrcode.make("This is my QRcode")
qr.save("myQR.png")
#running this generates the QRcode which stores This is my QRcode, and saves it in the same folder as the program


#Adjustable QRcode
qr = qrcode.QRCode(box_size =15)   #this parameter controls the QRcode image size

data = "https://www.google.co.uk/" #if someone scans this QRcode it will take them to the google webpage
qr.add_data(data)
qr.make(fit=True) #if you want to automatically adjust the QRcode dimension size
img = qr.make_image()
img.save("2ndQRcode.png")
#this would generate a larger QR code and stores the link to google search website
