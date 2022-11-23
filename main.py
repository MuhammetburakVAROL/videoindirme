import os.path
from pytube import YouTube

def videoindirme():

 while True:
  print("Çıkış yapmak için x'i tuşlayınız.")
  exit = input("Çıkış yapmak istiyor musunuz? ")
  if exit == "x":
      print("uygulamadan çıkılıyor...")
      break
  link = input("Link: ")
  klasor = input("klasor: ")

  try:
      yt = YouTube(link)
  except:
      print("hatalı link")
      exit()

  mp3 = yt.streams.filter(only_audio = True).first()

  print("İndiriliyor...")

  output = mp3.download(klasor)

  base, ext = os.path.splitext(output)
  to_mp3 = base + ".mp3"
  os.rename(output, to_mp3)

videoindirme()