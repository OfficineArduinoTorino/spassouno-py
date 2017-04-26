import random
import pygame
from camera import Camera
from frame_manager import FrameManager
import testi
from pygame.locals import *
import time
import os


def keyboard_interaction():
	global current_text_tag,last_time_text,animation_speed,NEXT_CRITICAL_ACTION
	for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
				elif event.key == pygame.K_SPACE:
					camera.save_frame(frameManager)
					current_text_tag="scattato"
				elif event.key == pygame.K_UP:
					NEXT_CRITICAL_ACTION="changetosession"+str(frameManager.current_session+1)
					current_text_tag="cambio sessione"
				elif event.key == pygame.K_DOWN:
					NEXT_CRITICAL_ACTION="changetosession"+str(frameManager.current_session-1)
					current_text_tag="cambio sessione"
				elif event.key == pygame.K_x:
					frameManager.remove_frame()
					current_text_tag="rimosso"
				elif event.key == pygame.K_s:
					NEXT_CRITICAL_ACTION="save"
					current_text_tag="saving"
				elif event.key == pygame.K_r:
					camera.ruota()
				elif event.key == pygame.K_DELETE:
					frameManager.delete_all()
				elif event.key == pygame.K_BACKSPACE:
					frameManager.delete_current_scene()
				elif event.key == pygame.K_p:
					animation_speed/=2.0
					if animation_speed<0.003125:
						animation_speed=0.003125
				elif event.key == pygame.K_o:
					animation_speed*=2.0
					if animation_speed>3.2:
						animation_speed=3.2
				else:
					for n in range(10):
						if event.key == pygame.__dict__["K_"+str(n)]:
							nf=n-1
							if nf<0:
								nf=9
							NEXT_CRITICAL_ACTION="changetosession"+str(nf)
							current_text_tag="cambio sessione"
				last_time_text=time.time()


def critical_action_manager():
	global NEXT_CRITICAL_ACTION,current_text_tag
	if NEXT_CRITICAL_ACTION=="save":
		ok=frameManager.save()
		if ok:
			current_text_tag="salvato"
		else:
			current_text_tag="no usb"

	for n in range(frameManager.number_of_sessions):
		if NEXT_CRITICAL_ACTION=="changetosession"+str(n):
			frameManager.load_session(n)
			current_text_tag="sessione cambiata"

	NEXT_CRITICAL_ACTION=None






pygame.init()
display = pygame.display.set_mode((1680,1050),pygame.FULLSCREEN)
#display = pygame.display.set_mode((640,480),pygame.FULLSCREEN)

pygame.mouse.set_visible(False)

frame=pygame.surface.Surface((display.get_width()/2,display.get_height()/2), 0, display)

logo=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)),"logoSpassoUno.jpeg"))
logo=pygame.transform.scale(logo,(display.get_width()/8,int(display.get_height()/7.5)))

camera=Camera((display.get_width(),display.get_height()),display)
frameManager=FrameManager()

last_time=time.time()
last_time_text=time.time()
animation_speed=0.1
#used to write warning text before doing operations that freeze the software
NEXT_CRITICAL_ACTION=None

current_text_tag="tutorial"

image=camera.frame

testi.load_text_it(frameManager,display.get_width())

if camera.is_picamera:
	y=display.get_height()/4
	camera.camera.start_preview(fullscreen=False,window=(0,y,display.get_width()/2,display.get_height()/2))

def draw_frame_position(pos,width):
	if len(frameManager.images)==0:
		step_pos=pos[0]
	else:
		step_pos=pos[0]+(width*frameManager.current_frame)/len(frameManager.images)
	
	pygame.draw.line(display, (255,255,255), (pos[0],pos[1]-20), (pos[0],pos[1]+20))
	pygame.draw.line(display, (255,255,255), (pos[0]+width,pos[1]-20), (pos[0]+width,pos[1]+20))
	pygame.draw.line(display, (255,255,255), (pos[0],pos[1]), (pos[0]+width,pos[1]))
	pygame.draw.line(display, (255,0,0), (step_pos,pos[1]-20), (step_pos,pos[1]+20), 3)
	
def draw_text():
	global current_text_tag
	
	if time.time()-last_time_text>10.0:
		current_text_tag="tutorial"
		
	testi.draw(display,current_text_tag,(display.get_width()/2,(display.get_height()*7)/8),horiz="center",vert="center")

while True:
	keyboard_interaction()

	display.fill((0,100,255))

	display.blit(logo,((display.get_width()-logo.get_width())/2,5))

	if not camera.is_picamera:
		if camera.camera.query_image():
			image = camera.camera.get_image(camera.frame)

	aspect_ratio=float(image.get_width())/image.get_height()

	image=pygame.transform.scale(image, (display.get_width()/2, int((display.get_width()/2)/aspect_ratio)))
	display.blit(image,(0,(display.get_height()-image.get_height())/2))

	if time.time()-last_time>animation_speed:
		last_time=time.time()
		frame=frameManager.get_next_frame()
		if frame == None:
			frame=pygame.surface.Surface((display.get_width()/2,display.get_height()/2), 0, display)
		else:
			frame=pygame.transform.scale(frame, (display.get_width()/2, int((display.get_width()/2)/aspect_ratio)))
	
	display.blit(frame,(display.get_width()/2,(display.get_height()-frame.get_height())/2))

	#display current session number
	testi.draw(display,"session"+str(frameManager.current_session),(display.get_width()-10,20),horiz="right")
	#display current frame number
	draw_frame_position((display.get_width()/2,display.get_height()/5),display.get_width()/2-10)
	#display current text:
	draw_text()
	
	pygame.display.update()

	critical_action_manager()



pygame.quit()
if camera.is_picamera:
	camera.camera.stop_preview()
