import os

path = os.chdir("F:\\Hrithik Muttin Academic Space\\007 Skills007\\automated_youtube_channel-master\\Downloaded Reels")
i=1;
for file in os.listdir(path):
    new_file_name = "Amazon Flipkart Myntra Deals Fetcher on Telegram For Indian Shopping Sites Link In Description {}.mp4".format(i)
    os.rename(file,new_file_name)
    i += 1
