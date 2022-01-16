import scrape_videos
import os

try:
    os.remove("Downloaded Reels/Amazon Flipkart Myntra Ajio Deals Fetcher on Telegram For Indian Shopping Sites Link In Description.mp4")
except:
    print('Ntg to Delete')
scrape_videos.scrapeVideos(username = "deals_fetcher_telegram",
                     password = "python007",
                     output_folder = "Downloaded Reels/",days=5 )

import merge
import youtube_uploader

