#twitterpull: Pull tweets, removes current images, and stores new images in the given directory

import wget #python -m pip install wget
import tweepy #python -m pip install tweepy
import os

#Set up a class tweet_processor to handle all functions, inputs and outputs connected to the main script
class tweet_processor:

	#Initialize important variables to be used within class (List to store tweets, api, screen name)
	def __init__(self):
		self.all_tweets = []
		self.api = None
		self.screen_name = None
		print("Tweet process initialized")

	#Verify key credentials and set api and screen_name variables within the class
	def twitter_verify(self, consumer_key, consumer_secret, access_key, access_secret, screen_name):
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_key, access_secret)
		self.api = tweepy.API(auth)
		self.screen_name = screen_name
		print("Keys Authenticated")

	#Pull tweets by
		# Making a list to store tweets 
		# Requesting 10 initial tweets from a twitter profile 
		# Adding these tweets to the list 
		# Saving the ID of the oldest tweet
		# Repeating process if there are more (max is 50 tweets)
	# EXCEPTION: If the twitter account is private/doesn't exist, or if twitter/internet is not responding:
		# Ask user to check connection, ask again for an account name and use recursion
	def pull_tweets(self):
		try:
			new_tweets = self.api.user_timeline(screen_name = self.screen_name, count = 10)
			self.all_tweets.extend(new_tweets)
			oldest = self.all_tweets[-1].id - 1
			while len(new_tweets) > 0:
				new_tweets = self.api.user_timeline(screen_name = self.screen_name, count = 10, max_id = oldest)
				self.all_tweets.extend(new_tweets)
				oldest = self.all_tweets[-1].id - 1
				if len(self.all_tweets) >= 50:
					break
		except tweepy.TweepError:
			print("-> ERROR OCCURRED. Possible reasons:")
			print("-> Twitter or your internet is not responding")
			print("-> OR")
			print("-> The account you entered is private or doesn't not exist")
			print("-> Please check your connection and insert a new screen name (otherwise Ctrl+C to exit)")
			self.screen_name = input()
			self.pull_tweets()
		print("%s tweets obtained" % len(self.all_tweets))

	#If there are old images(not obtained from the current pull), remove them so they won't be used for the video
	def remove_old_images(self):
		for image_name in os.listdir('.'):
			if image_name.endswith('.jpg'):
				os.remove(image_name)
		print("Old images removed in directory")

	#Check the entities property of a tweet to see if there is a media object (image related)
	#If there is, get the URL for these images and put these images into a set 
	#For each image, set the filename to image-00x.jpg, with x being a running counter
	#Download to directory via wget
	def store_new_images(self):
		pictures = set()
		if len(self.all_tweets) > 0: 
			for selected_tweet in self.all_tweets:
				media_ob = selected_tweet.entities.get('media',[])
				if(len(media_ob) > 0):
					image_link = media_ob[0]['media_url']
					pictures.add(image_link)
			print("%s images obtained" % len(pictures))
			image_counter = 0
			for selected_picture in pictures:
				image_counter += 1 
				file_name = ("image-%03d.jpg" % image_counter)
				wget.download(selected_picture, file_name)
				print('%s downloaded' % file_name)
			print("New images stored in directory")
		else:
			print("No new images found from twitter feed")