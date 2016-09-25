# Author: Yuze Bob Ma
# Date: Sept, 24th, 2016
# This code is written for Lab 4

from PIL import Image


two_by_two_wallpaper = Image.new('RGB',(512,512))


# ca = Caption America
# im = Iron Man
# hk = Hork
# bw = Black Widow
ca = Image.open('ca.jpg').resize((256,256))
im = Image.open('im.jpg').resize((256,256))
hk = Image.open('hk.jpg').resize((256,256))
bw = Image.open('bw.jpg').resize((256,256))

two_by_two_wallpaper.paste(ca,(0,0))
two_by_two_wallpaper.paste(im,(256,0))
two_by_two_wallpaper.paste(hk,(0,256))
two_by_two_wallpaper.paste(bw,(256,256))
two_by_two_wallpaper.show()
# two_by_two_wallpaper.save('LOL.jpg')