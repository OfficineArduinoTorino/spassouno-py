import random
import pygame
import os
class FrameManager():
	def __init__(self):
		self.number_of_sessions=10
		self.current_session=0
		self.current_frame=0
		self.path=os.path.join(os.path.dirname(os.path.realpath(__file__)),"images")
		self.images=[]
		if not os.path.isdir(self.path):
			os.makedirs(self.path)
		for i in range(self.number_of_sessions):
			p=os.path.join(self.path,str(i))
			if not os.path.isdir(p):
				os.makedirs(p)

		self.load_session(self.current_session)

	def get_current_session_path(self):
		return os.path.join(self.path,str(self.current_session))

	def save_image(self,image):
		filename=os.path.join(self.get_current_session_path(),"frame_"+"0"*(5-len(str(len(self.images))))+str(len(self.images))+".jpeg")
		pygame.image.save(image,filename)
		image=pygame.image.load(filename)
		self.images.append(image)

	def load_session(self,number):
		if number>=self.number_of_sessions:
			number=0
		if number < 0:
			number=self.number_of_sessions-1
		self.current_session=number
		files=[f for f in os.listdir(self.get_current_session_path()) if os.path.isfile(os.path.join(self.get_current_session_path(), f))]
		files.sort()
		
		self.images=[]
		for f in files:
			self.images.append(pygame.image.load(os.path.join(self.get_current_session_path(), f)))

		self.current_frame=len(self.images)-1

	def get_next_frame(self):
		if len(self.images)==0:
			return None
		self.current_frame+=1
		if self.current_frame>=len(self.images):
			self.current_frame=0
		return self.images[self.current_frame]

	def remove_frame(self):
		if len(self.images)==0:
			return

		self.images=self.images[0:-1]
		files=[f for f in os.listdir(self.get_current_session_path()) if os.path.isfile(os.path.join(self.get_current_session_path(), f))]
		files.sort()
		os.remove(os.path.join(self.get_current_session_path(),files[-1]))

	def delete_current_scene(self):
		self.images=[]
		files=[f for f in os.listdir(self.get_current_session_path()) if os.path.isfile(os.path.join(self.get_current_session_path(), f))]
		for f in files:
			os.remove(os.path.join(self.get_current_session_path(),f))

	def delete_all(self):
		self.images=[]
		for s in range(self.number_of_sessions):
			self.current_session=s
			self.delete_current_scene()
		self.current_session=0

	def save(self):
		if len(self.images)==0:
			return
			
		if self.is_usb_plugged():
			path = self.get_current_session_path()
			#os.system("convert -delay 20 -loop 0 "+path+"/*.jpeg /media/usb0/movie"+str(self.current_session)+".mpeg")
			#gst-launch-1.0 multifilesrc location=timelapse%04d.jpeg index=1 caps="image/jpeg,framerate=24/1" ! jpegdec ! omxh264enc ! avimux ! filesink location=timelapse.avi
			os.system("gst-launch-1.0 multifilesrc location="+path+"/frame_%05d.jpeg index=0 caps=\"image/jpeg,framerate=24/1\" ! jpegdec ! omxh264enc ! avimux ! filesink location=/media/usb0/movie"+str(self.current_session)+".avi")
			#os.system("gst-launch-1.0 multifilesrc location="+path+"/frame_%05d.jpeg index=0 caps=\"image/jpeg,framerate=24/1\" ! jpegdec ! omxh264enc ! avimux ! filesink location=timelapse.avi")
		else:
			print "please Insert USB Drive and Retry"
			return False
		return True

	def is_usb_plugged(self):
		partitionsFile = open("/proc/partitions")
		lines = partitionsFile.readlines()[2:]#Skips the header lines
		for line in lines:
			words = [x.strip() for x in line.split()]
			minorNumber = int(words[1])
			deviceName = words[3]
			if minorNumber % 16 == 0:
				path = "/sys/class/block/" + deviceName
				if os.path.islink(path):
					if os.path.realpath(path).find("/usb") > 0:
						#return "/dev/%s" % deviceName
						return True
		return False
