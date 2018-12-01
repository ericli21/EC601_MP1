#convertvid: Delete any current videos, Convert current images into a new video (foo.mp4)
import subprocess
import os
from PIL import Image

#Set up a class ff_processor to handle ffmpeg functions and variables
class ff_processor:

	#Initialize important input variables (framerate, video file name)
	def __init__(self):
		self.framerate_piece = None
		self.endfile_piece = None
		print("FFMPEG process initialized")

	def ff_framerate(self, framerate):
		self.framerate_piece = " -framerate %f" % framerate

	def ff_endfile(self, endfile):
		self.endfile_piece = " %s.mp4" % endfile

	#If there is already a video in the directory, delete it to avoid a overwrite option select
	def delete_old_video(self):
		for video_name in os.listdir('.'):
			if video_name.endswith('.mp4'):
				os.remove(video_name)
		print("Old videos removed from directory")

	#To create a video in bash: the general command to convert is:
	#ffmpeg -f image2 -framerate 12 -i 'foo-*.jpg' foo.mp4
	#-pattern_type glob is used to put the images in order for the video
	#-vf 1350:-2 is to avoid an error where FFMPEG tries to compress and divide a side with an odd number of pixels by 2
	#-vf will compress the width to 1350 pixels and the height will fit the same aspect ratio but divisble by 2
	#In Python, subprocess is used to execute this command
	def create_new_video(self):
		process_string = "ffmpeg -f image2 -i image-%03d.jpg -pattern_type glob -vf 1350:-2"
		if self.framerate_piece is not None:
			process_string += self.framerate_piece
		if self.endfile_piece is not None:
			process_string += self.endfile_piece
		else:
			print("-> ERROR OCCURRED. Possible reasons:")
			print("-> Video name not entered. Please enter a name (without the .mp4)")
			self.endfile_piece = input()
			self.create_new_video()
		subprocess.check_call('ffmpeg -f image2 -framerate 0.1 -i image-%03d.jpg foo.mp4')
		print("Video converted")
