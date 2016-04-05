#!/usr/bin/env python

from PIL import Image
import sys, os

images = []
frameDuration = 0.5

for i in range(1,3):
	filename = "./res/testImg/dove"+str(i)+".jpg"
	images.append(Image.open(filename))

from images2gif import writeGif
writeGif("out.gif", images, duration=frameDuration, dither=0)