import os
import youtube_uploader
import scrape_videos
import videoDetails

path = r"F:/Hrithik Muttin Academic Space/007 Skills007/automated_youtube_channel-master/Downloaded Reels/"

scrape_videos.scrapeVideos(username = "deals_fetcher_telegram",
                     password = "python007",
                     output_folder = "Downloaded Reels/",days=1 )

import rename

args = videoDetails.Video()
youtube = youtube_uploader.get_authenticated_service()
# youtube_uploader.initialize_upload(youtube, args)

for file in os.listdir(path):
    if( '.json' in file):
        print('Its A JSON FILE')
    else:
        os.chdir(r"F:\Hrithik Muttin Academic Space\007 Skills007\automated_youtube_channel-master")
        # args = videoDetails.Video()
        # youtube = youtube_uploader.get_authenticated_service()
        youtube_uploader.initialize_upload(youtube, args)
        os.remove(path+file)
