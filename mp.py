from pyyoutube import Api
import pytube
import urllib.request
import os
import time
from googleapiclient.discovery import build

''' Environment variable setting '''
APIKey = 'you api key'
PlayListId = 'The playlist id'
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

def DownloadAndConvert(vid, vtitle, count):
    itemurl = 'https://www.youtube.com/watch?v=' + vid
    print('Downloading video', count, '/', itemCounts , ':', vid, '/',vtitle,'...')
    try:
        yt = pytube.YouTube(itemurl)
        yt.streams.first().download(filename=vid)
    except:
        print("下載"+vtitle+"時發生錯誤...")
    time.sleep(1)
    ''''''
    try:
        mp4 = VideoFileClip(vid+'.mp4')
        mp4.audio.write_audiofile(vtitle+'.mp3')
        os.remove(vid+'.mp4')
    except:
        print("轉檔"+vtitle+"時發生錯誤...")
from pytube import YouTube
import multiprocessing as mp
from multiprocessing import Pool


with Pool(3) as pool:
    for vid, vtitle in itemList:
        count = count + 1
        pool.apply_async(
            DownloadAndConvert, args=(vid, vtitle, count,), error_callback=lambda e: print(e)
        )
    pool.close()
    pool.join()
