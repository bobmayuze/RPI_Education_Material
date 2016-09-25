# Author: Yuze Bob Ma
# Date: Sept, 24th, 2016
# This code is written for Lab 4

from PIL import Image
import Part_2_helper as P2h


two_by_two_wallpaper = Image.new('RGB',(512,512))


# ca = Caption America
# im = Iron Man
# hk = Hork
# bw = Black Widow
ca = Image.open('ca.jpg')
im = Image.open('im.jpg')
hk = Image.open('hk.jpg')
bw = Image.open('bw.jpg')

ca_square = P2h.make_square(ca)
im_square = P2h.make_square(im)
hk_square = P2h.make_square(hk)
bw_square = P2h.make_square(bw)


ca_square = ca_square.resize((256,256))
im_square = im_square.resize((256,256))
hk_square = hk_square.resize((256,256))
bw_square = bw_square.resize((256,256))



two_by_two_wallpaper.paste(ca_square,(0,0))
two_by_two_wallpaper.paste(im_square,(256,0))
two_by_two_wallpaper.paste(hk_square,(0,256))
two_by_two_wallpaper.paste(bw_square,(256,256))
two_by_two_wallpaper.show()
# two_by_two_wallpaper.save('LOL.jpg')