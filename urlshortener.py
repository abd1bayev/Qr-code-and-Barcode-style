import pyperclip
import pyshorteners

def shortener(url):
  sh_url = pyshorteners.Shortener()
  sh_url = sh_url.tinyurl.short(url)
  pyperclip.copy(sh_url[8:])
  print('\nText copied to clipboard')

#If for some reason you want to save your output in a txt file, add this function to main
'''
def shortener_saver(sh_url):
  file = open("shortURLs.txt", "a")
  file.write(f"{sh_url}\n")
  print(f"URL written in shortURLs text archive on {os.getcwd()}")
  file.close()
'''