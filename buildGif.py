#!/usr/bin/env python

import imageio

filenames=[]
for i in range(2):
	filenames.append("res/testImg/dove"+str(i+1)+".jpg")

with imageio.get_writer('movie.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)