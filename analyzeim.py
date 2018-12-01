#analyzeim: Feed images to the Google Vision API and obtain annotations (aka labels), removes current labels, stores new labels
import io
import os
import google
from google.oauth2 import service_account
from google.cloud import vision #python -m pip install google-cloud-vision

#Set up a class google_processor to handle all functions, inputs and outputs connected to the main script
class google_processor:

	#Initialize important variables to be used within class (Crendentials, labels)
	def __init__(self):
		self.credentials = None
		self.all_labels = []
		print("Vision process initialized")

	#Get key credentials from the JSON file
	def google_verify(self, json_file):
		self.credentials = service_account.Credentials.from_service_account_file(json_file)
		print("JSON file autheticated")
		
	#Use credentials to create a "client" for using Google Vision
	#Find images within directory and obtain annotations/labels using the Google Vision
	#Concatenate the labels into one sentence and store the sentence in all_labels
	#If no images are found, the process will keep running but a message will pop up
	#EXCEPTION: If Google or the internet is down:
		#The program will output a message to try again
	def get_annotations(self):
		try:
			client = vision.ImageAnnotatorClient(credentials = self.credentials)
			counter = 0
			for image_name in os.listdir('.'):
				if image_name.endswith('.jpg'):
					with io.open(image_name, 'rb') as image_file:
						content = image_file.read()
					image = vision.types.Image(content = content)
					response = client.label_detection(image = image)
					labels = response.label_annotations
					counter += 1
					sentence = "Frame %03d labels:" % counter
					for label in labels:
						sentence = sentence + " " + label.description
					self.all_labels.append(sentence)
			if counter == 0:
				print("No annotations obtained (no images found)")
			else:
				print("Annotations obtained")
		except google.api_core.exceptions.ServiceUnavailable:
			print("-> ERROR OCCURRED. Possible reasons:")
			print("-> Google or your internet is not responding")
			print("Try again? (y/n)")
			answer = input()
			if answer == 'y':
				self.get_annotations()
			else:
				raise

	#If there are old labels in a labels.txt (not obtained from the current pull), remove the file
	def remove_old_labels(self):
		for label_name in os.listdir('.'):
			if label_name.endswith('labels.txt'):
				os.remove(label_name)
		print("Old label.txt removed")

	#Take the stored sentences with labels and write them to labels.txt
	#If there are no images/annotations, an empty labels.txt will appear
	def store_new_labels(self):
		file_name = "labels.txt"
		file1 = open(file_name, "w")
		if len(self.all_labels) > 0:
			for sentence in self.all_labels:
				file1.write(sentence + "\n" + "\n")
			file1.close()
			print("Labels stored in new %s" % file_name)
		else:
			print("No images: empty %s" % file_name)
