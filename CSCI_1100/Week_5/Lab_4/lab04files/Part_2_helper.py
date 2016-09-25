# Author: Yuze Bob Ma
# Date: Sept, 24th, 2016
# This code is written for Lab 4

from PIL import Image

def make_square(img):
	im = img
	width = im.size[0]
	height = im.size[1]
	print(width, height)
	if width > height:
		im_new = im.crop((0,0,height,height))
	else:
		im_new = im.crop((0,0,width,width))
	return im_new

