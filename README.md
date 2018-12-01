# EC601 Mini Project 1 Submission - Eric Li
This is my library/API for Mini Project 1. The purpose of this set of code is to pull image data from a twitter feed into the current directory, describe these images using Google Vision labels (stored into a text file in the directory), and combining the images into a video through FFMPEG. MiniProject1.py is a main script that shows how to use all the functions in each library.

## Setup
In order to run the main script, open your terminal (I used git bash) and cd into your folder containing the files. In the bash, type: 
```
python MiniProject1.py
```
Please note that you should put your own API keys in MiniProject1.py to run successfully. Make sure that your environment variable in bash include your python.exe and FFMPEG.exe files. Keep the folder clear of any images, text files or videos, as they will be replaced with new files everytime you run the main script. Please also note that you should never give out API keys to anyone/ on GitHub. 

## Additional Notes
The max number of tweets that can be pulled is set to 50. This is to prevent going over the rate limit. When creating a video, there may be a strange delay in the beginning, showing nothing but a black screen. However, it will later show the images in order.

## Sources
1. https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object.html#media
2. https://cloud.google.com/python/
3. https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate
4. https://docs.python.org/3/library/subprocess.html
5. https://ffmpeg.org/ffmpeg.html