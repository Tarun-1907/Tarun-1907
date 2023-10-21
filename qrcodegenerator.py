import pyqrcode 
import png

from pyqrcode import QRCode
link_name='www.Myqrcode.com'
generate=pyqrcode.create(link_name)

generate.png('qr.png',scale=10)
generate.svg('qr.svg',scale=10)

print("Your QR code is generated. Thank you")