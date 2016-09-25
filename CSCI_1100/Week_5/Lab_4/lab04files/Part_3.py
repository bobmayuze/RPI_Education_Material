# Author: Yuze Bob Ma
# Date: Sept, 24th, 2016
# This code is written for Lab 4

from PIL import Image
# import Part_2_helper as P2h


two_by_two_wallpaper = Image.new('RGB',(1000,360))


# ca = Caption America
# im = Iron Man
# hk = Hork
# bw = Black Widow
im_1 = Image.open('1.jpg')
im_2 = Image.open('2.jpg')
im_3 = Image.open('3.jpg')
im_4 = Image.open('4.jpg')
im_5 = Image.open('5.jpg')
im_6 = Image.open('6.jpg')


# Resize these pictures
im_1 = im_1.resize((int(im_1.size[0]*round(256/im_1.size[1],2)),256))
im_2 = im_2.resize((int(im_2.size[0]*round(256/im_2.size[1],2)),256))
im_3 = im_3.resize((int(im_3.size[0]*round(256/im_3.size[1],2)),256))
im_4 = im_4.resize((int(im_4.size[0]*round(256/im_4.size[1],2)),256))
im_5 = im_5.resize((int(im_5.size[0]*round(256/im_5.size[1],2)),256))
im_6 = im_6.resize((int(im_6.size[0]*round(256/im_6.size[1],2)),256))



two_by_two_wallpaper.paste(im_1,(31,20))
two_by_two_wallpaper.paste(im_2,(10+31+int(im_1.size[0]*round(256/im_1.size[1],2)),60))
two_by_two_wallpaper.paste(im_3,(2*10+31+2*int(im_1.size[0]*round(256/im_1.size[1],2)),20))
two_by_two_wallpaper.paste(im_4,(3*10+31+3*int(im_1.size[0]*round(256/im_1.size[1],2)),60))
two_by_two_wallpaper.paste(im_5,(4*10+31+4*int(im_1.size[0]*round(256/im_1.size[1],2)),20))
two_by_two_wallpaper.paste(im_6,(5*10+31+5*int(im_1.size[0]*round(256/im_1.size[1],2)),60))
two_by_two_wallpaper.show()
# two_by_two_wallpaper.save('LOL.jpg')