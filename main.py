from pyyoutube import Api
import pytube
import urllib.request
import os
from googleapiclient.discovery import build

''' Environment variable setting '''
APIKey = 'your youtube api key'
PlayListId = 'Youtube playlist id'
PlayListContentNums = 200 #The number of videos in this playlist
''' Environment varialbe setting '''

api = Api(api_key=APIKey)
playlist_item = api.get_playlist_items(playlist_id=PlayListId, count = PlayListContentNums)

# Get item id and title
itemList = []
for item in playlist_item.items:
    itemList.append([item.snippet.resourceId.videoId, item.snippet.title])

# Download videos and transfer to MP3
from moviepy.editor import *

itemCounts = len(itemList)
print("==================================")
print(itemCounts," videos found.")
print("==================================")
count = 0
videoSubFolder = './Video'
from pytube import YouTube
for vid, vtitle in itemList:
    count = count + 1
    itemurl = 'https://www.youtube.com/watch?v=' + vid
    print('Downloading video', count, '/', itemCounts , ':', vid, '/',vtitle,'...')
    try:
        yt = pytube.YouTube(itemurl)
        mp4 = VideoFileClip(vtitle+'.mp4')
        mp4.audio.write_audiofile(vtitle+'.mp3')
        os.remove(vtitle+'.mp4')
    except:
        print("Error... QQ... ")
        count = count - 1
