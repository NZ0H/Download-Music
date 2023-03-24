import os
from pytube import YouTube

# Recovering the video

url = YouTube(str(input("Put the URL of the music : ")))
video = url.streams.filter(only_audio=True).first()

print("Here is the music you want to download : " + url.title)

# The music is installed in the same place as the python file
vid_dow = video.download(output_path='.')
title , format = os.path.splitext(vid_dow)

# Change of the file format
name_file = title + '.mp3'
os.rename(vid_dow , name_file)

print("The sound has been downloaded !")
