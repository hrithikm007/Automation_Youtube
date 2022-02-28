#from moviepy.editor import *
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

FOLDER_PATH = r"F:/Hrithik Muttin Academic Space/007 Skills007/automated_youtube_channel-master/Downloaded Reels/"
videos_in_path = []


def listDir(dir):
    filenames = os.listdir(dir)
    for x in filenames:
        if (x != 'thumbnail.jpg'):
            # print("File Name is "+x)
            # print("Folder Path "+ os.path.abspath(os.path.join(dir,x)),sep='\n')
            videos_in_path.append(os.path.abspath(os.path.join(dir,x)))

if __name__!='__main__':  #IMPORTANT HERE MADE IF NAME NOT EQUAL TO MAIN
    listDir(FOLDER_PATH)

# clip1 = VideoFileClip("Downloaded Reels/2742088437612186144-hrithikm007-750-1333.mp4")
# clip2 = VideoFileClip("Downloaded Reels/2740934573986994009-hrithikm007-750-1333.mp4")
# final_clip = concatenate_videoclips([clip1,clip2])
# final_clip.write_videofile("Downloaded Reels/my_concatenation.mp4")

    clips = []
    for x in videos_in_path:
        clips.append(VideoFileClip(x))
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("Downloaded Reels/Amazon Flipkart Myntra Deals Fetcher on Telegram For Indian Shopping Sites Link In Description.mp4")
    # videos_in_path.remove('F:\Hrithik Muttin Academic Space\Skills007\automated_youtube_channel-master\Downloaded Reels\thumbnail.jpg')
    for x in videos_in_path:
        os.remove(x)
