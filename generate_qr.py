import os
import qrcode
from tkinter import colorchooser
import tkinter as tk
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask


#Defines if the QR code is gonna be colorized or not.
def wants_color() -> bool:
  wc = input('''
Do you want to colorize your QR code?
1. Yes
2. No
>> ''')
  if wc == '1' or wc == 'yes' or wc == 'y':
    print("\nOpening color picker window")
    return True
  elif wc == '2' or wc == 'no' or wc =='n':
    return False
  else:
    print("Choose a VALID option.\n")
    wc = wants_color()

#Color mask
def colorized():
  if wants_color():
    color=RadialGradiantColorMask(center_color=center_color(), edge_color=edge_color())
    return color
  else:
    nocolor=RadialGradiantColorMask(center_color=(0, 0, 0), edge_color=(0, 0, 0))
    return nocolor

#If colorized, defines the CENTER color
def center_color():
  center = colorchooser.askcolor(title='Choose center color')
  center = center[0]
  return center

#If colorized, defines a color for the EDGES
def edge_color():
  edge = colorchooser.askcolor(title='Choose border color')
  edge = edge[0]
  return edge

#Chooses the QR code style.
def choose_qr_style():
  st = int(input('''
Choose a QRcode Style:
1. Square (Normal) 
2.Gapped Square
3.Vertical Bars
4.Horizontal Bars
5.Circles
6.Rounded
>> '''))
  if st == 1:
    return SquareModuleDrawer()
  elif st == 2:
    return GappedSquareModuleDrawer()
  elif st == 3:
    return VerticalBarsDrawer()
  elif st == 4:
    return HorizontalBarsDrawer()
  elif st == 5:
    return CircleModuleDrawer()
  elif st == 6:
    return RoundedModuleDrawer()
  else:
    print("Choose a VALID option.\n")
    st = choose_qr_style()

#QR code generation
def gen_qr(url):
  qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
  qr.add_data(url)
  img = qr.make_image(image_factory=StyledPilImage, module_drawer=choose_qr_style(),
                      color_mask=colorized())
  return img

#Saving the generated QR code
def save_qr(img):
  imgnumber = 0
  while os.path.exists(f'QR{imgnumber}.png'):
    imgnumber += 1
  img.save(f'QR{str(imgnumber)}.png')
  print(f'\nGenerated QR{imgnumber}.png on {os.getcwd()}')

