#!/usr/bin/env python
# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
import random
import pygame
import os

it={}
de={}
en={}

font1={}
font1["path"]=os.path.join(os.path.dirname(os.path.realpath(__file__)),"DKLemonYellowSun.otf")

colore_testi=pygame.Color(255,255,255)

def create_text(text, font, size, color, length=-1):
	text = unicode(text,"utf-8")
	out=[]
	if not str(size) in font:
		font[str(size)]=pygame.font.Font(font["path"], size)
	
	final_lines = []

	requested_lines = text.splitlines()

	if length<0:
		for t in requested_lines:
			out.append(font[str(size)].render(t,0,color))

		return out

	# Create a series of lines that will fit on the provided
	# rectangle.

	for requested_line in requested_lines:
		if font[str(size)].size(requested_line)[0] > length:
			words = requested_line.split(' ')
			# if any of our words are too long to fit, return.
			for word in words:
				if font[str(size)].size(word)[0] >= length:
					raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
			# Start a new line
			accumulated_line = ""
			for word in words:
				test_line = accumulated_line + word + " "
				# Build the line while the words fit.	
				if font[str(size)].size(test_line)[0] < length:
					accumulated_line = test_line 
				else: 
					final_lines.append(accumulated_line) 
					accumulated_line = word + " " 
			final_lines.append(accumulated_line)
		else: 
			final_lines.append(requested_line) 


	for t in final_lines:
		out.append(font[str(size)].render(t,0,color))

	return out


def draw(screen,text,pos,horiz="left",vert="top",interlinea=1.0):
	n_lines=0

	actual_text=it[text]

	tot_lines=len(actual_text)-1
	for render in actual_text:
		final_pos_x = pos[0]
		if horiz=="center":
			final_pos_x-=render.get_width()/2
		elif horiz=="right":
			final_pos_x-=render.get_width()

		final_pos_y = pos[1]
		if vert=="top":
			final_pos_y+=render.get_height()*n_lines
		elif vert=="bottom":
			final_pos_y-=render.get_height()*(tot_lines-n_lines)

		screen.blit(render,(final_pos_x,final_pos_y))

		n_lines+=1


def load_text_it(frame_manager,screen_width):
	global font1, it, colore_testi
	size=80*screen_width/1680

	it["tutorial"]=create_text("Premi il Pulsante Rosso per scattare una foto!",font1,size,colore_testi)
	it["scattato"]=create_text("BRAVO! hai appena scattato una foto!",font1,size,colore_testi)
	it["cambio sessione"]=create_text("sto caricando un'altra sessione, attendi...",font1,size,colore_testi)
	it["sessione cambiata"]=create_text("sei passato ad un'altra sessione",font1,size,colore_testi)
	it["rimosso"]=create_text("hai rimosso una foto",font1,size,colore_testi)
	it["saving"]=create_text("sto salvando, attendi...",font1,size,colore_testi)
	it["salvato"]=create_text("il tuo lavoro è stato SALVATO!",font1,size,colore_testi)
	it["no usb"]=create_text("inserisci una chiavetta usb per salvare!",font1,size,colore_testi)

	for i in range(frame_manager.number_of_sessions):
		it["session"+str(i)]=create_text("sessione "+str(i+1)+" di "+str(frame_manager.number_of_sessions),font1,size/2,colore_testi)
