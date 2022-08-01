from pytube import YouTube
from sys import argv

link = argv[2]    #the second input in terminal  (the link)
video = YouTube(link)

print("Video Title:", video.title)
print("Source:", video.channel_id)

stream = video.streams.get_highest_resolution()
stream.donwload("Path for the video installation")
print("Done")