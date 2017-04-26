import random
import pygame.camera
import os
import io
from PIL import Image
class Camera():
	def __init__(self,resolution,display):
		pygame.camera.init()
		self.resolution=resolution

		camlist = pygame.camera.list_cameras()
		if not camlist:
			import picamera
			self.is_picamera=True
			self.camera=picamera.PiCamera()
			self.camera.rotation = 270
		else:
			self.camera = pygame.camera.Camera(camlist[0],self.resolution)
			self.camera.start()
			self.is_picamera=False
			

		self.frame=pygame.surface.Surface(self.resolution, 0, display)

	def ruota(self):
		self.camera.rotation+=90
		if self.camera.rotation>=360:
			self.camera.rotation=0

	def save_frame(self,frame_manager):
		filename=os.path.join(frame_manager.get_current_session_path(),"frame_"+"0"*(5-len(str(len(frame_manager.images))))+str(len(frame_manager.images))+".jpeg")
		if self.is_picamera:			
			self.camera.capture(filename, use_video_port=True)
			'''stream = io.BytesIO()
			self.camera.capture(
				stream, use_video_port=True, format='jpeg')
			frame = Image.open(stream)
			frame.save(filename, "JPEG")'''
		else:
			if self.camera.query_image():
				self.frame = self.camera.get_image(self.frame)
			pygame.image.save(self.frame,filename)

		image=pygame.image.load(filename)
		frame_manager.images.append(image)			
