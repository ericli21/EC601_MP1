#Eric Li
#EC601: Mini-Project 3
#main script

import os
import twitterpull
import convertvid
import analyzeim
import databaseAPI

#Insert consumer and access information
#Twitter API credentials
consumer_key = "Insert consumer key"
consumer_secret = "Insert consumer secret"
access_key = "Insert access key"
access_secret = "Insert access secret"

#Google API credentials (filename.json)
json_file = "Insert path to filename.json"

#True = Store data in MongoDB, False = Store data in MySQL
def main(screen_name, db_choice, user_name):
	twitter_ob = twitterpull.tweet_processor()
	twitter_ob.twitter_verify(consumer_key, consumer_secret, access_key, access_secret, screen_name)
	twitter_ob.pull_tweets()
	twitter_ob.remove_old_images()
	twitter_ob.store_new_images()
	print("Image process done!\n")

	google_ob = analyzeim.google_processor()
	google_ob.google_verify(json_file)
	google_ob.get_annotations()
	google_ob.remove_old_labels()
	google_ob.store_new_labels()
	print("Analysis process done!\n")

	ff_ob = convertvid.ff_processor()
	ff_ob.ff_framerate(0.5)
	ff_ob.ff_endfile("foo")
	ff_ob.delete_old_video()
	ff_ob.create_new_video()
	print("Video process done!\n")	

	if db_choice == True:
		mongo_obj = databaseAPI.MongoTweets()
		mongo_obj.add_tweet(user_name, screen_name)
		mongo_obj.find_label('arch')
		mongo_obj.all_stats()
	else:
		mysql_obj = databaseAPI.MySQLTweets("root", "133221333123111", "TESTDB")
		mysql_obj.add_tweet(user_name, screen_name)
		mysql_obj.find_label('arch')
		mysql_obj.all_stats()
		mysql_obj.shut()

if __name__ == "__main__":
	main("@demasrusli", False, "rick")