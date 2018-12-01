# EC601 Mini Project 3 Submission - Eric Li
This is my library/API for Mini Project 3. The purpose of this set of code is to store image data that was pulled from a twitter feed into the current directory, as well as the Google Vision labels (stored into a text file in the directory) used to analyze these images. MiniProject3.py is a main script building off of the original script (MiniProject1.py) and shows how to use all the database functions in each library.

## Setup
In order to run the main script, open your terminal (I used git bash) and cd into your folder containing the files. In the bash, type: 
```
python MiniProject3.py
```
Please note that you should put your own API keys in MiniProject3.py to run successfully. Make sure that your environment variable in bash include your python.exe and FFMPEG.exe files. Keep the folder clear of any images, text files or videos, as they will be replaced with new files everytime you run the main script. Please also note that you should never give out API keys to anyone/ on GitHub. 

For setting up the databases, you may need to download and set up environments for (MongoDB)[https://www.mongodb.com/download-center] and (MySQL)[https://dev.mysql.com/downloads/mysql/]. For MongoDB, I downloaded the MongoDB package as well as Mongo Compass to visualize the database. I also used the pymongo API to connect to localhost and set up an admin account. For MySQL, I downloaded the python connector to MySQL, as well as the MySQL community server, shell and workbench. I used the pymysql API for working on this part.

For setting up admin and user privileges on MySQL, go to the MySQL shell as type:
```
\sql
\connect root@localhost
CREATE DATABASE TESTDB;
GRANT ALL PRIVILEGES ON TESTDB.* TO 'host'@'localhost';
```

## Additional Notes
The max number of tweets (and images) that can be pulled is set to 50. This is to prevent going over the rate limit. When creating a video, there may be a strange delay in the beginning, showing nothing but a black screen. However, it will later show the images in order.

The MongoDB and MySQL functions were intended to be similar: to store all images and labels, search which users had a certain label, and common label and image statistic. However, since both are different at handling data (specific lists and lists of lists), some features are left out from MySQL. The MongoDB is able to store image data (varying byte string length) and varying sizes of arrays, whereas in MySQL these variables had to be worked around by repeating image numbers, users, and handles for every single label. 

Additional directions to go into for this project would be to see how many times every user has used the system, as well as opening up images to show certain labels. 

## Sources
1. https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object.html#media
2. https://cloud.google.com/python/
3. https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate
4. https://docs.python.org/3/library/subprocess.html
5. https://ffmpeg.org/ffmpeg.html
6. https://www.w3schools.com/python/python_mongodb_getstarted.asp
7. https://www.tutorialspoint.com/python3/python_database_access.htm