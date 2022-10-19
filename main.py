from urlshortener import *
from generate_qr import *
import os

url = input('Enter a URL\n>> ')
print(os.getcwd())
def main():
  choose = int(input(
'''
Choose an option:
1. URL Shortener
2. QR Code Generator
>> '''
  ))
  if choose == 1:
    shortener(url)
  elif choose == 2:
    save_qr(gen_qr(url))
  else:
    print('Choose a VALID option')
    choose= main()

if __name__ == '__main__':
  main()