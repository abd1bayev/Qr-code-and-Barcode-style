"""
Just an quick implementation for a fully private QR code generator.
"""

import qrcode
from string import punctuation

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

print('Text to QR-tify:')
input_data = input()
qr.add_data(input_data)
qr.make(fit=True)
print('select colors:\n(1)QR Code Color\n(2)Background color')



colors = ['pink','orange','red','blue','green','grey','black','white','mediumvioletred','tomato','brown','mediumseagreen','darkslategray','indigo','darksalmon','cyan','palevioletred','darkcyan','firebrick','darkolivegreen','forestgreen','darkslateblue','olive','greenyellow','lime','wheat','gold']
available = ', '.join(sorted(colors)).upper()

print(f'Color ideas: {available}.')

print('\nSelect code color:')
qr_color = input().lower()
# while qr_color not in colors:
    # qr_color = input()

print('\nSelect background color:')
qr_back = input().lower()
# while qr_back not in colors:
#     qr_back = input()

# create img file
img = qr.make_image(fill_color=qr_color, back_color=qr_back)

# Save file -> name from QR input
title = ''
for el in input_data[:50]:
    if el not in punctuation:
        if not el.isspace():
            title+=el
        else:
            title+='_'

# Save QR code
img.save(f'{title[:5]}.png')