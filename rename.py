import os

path = os.chdir("F:\\Hrithik Muttin Academic Space\\007 Skills007\\automated_youtube_channel-master\\Downloaded Reels")

if __name__!='__main__':
    i=1;
    for file in os.listdir(path):
        new_file_name = "Amazon Flipkart Myntra Deals Fetcher on Telegram For Indian Shopping Sites Link In Description {}.mp4".format(i)
        if(file == 'client_secrets.json'):
            continue
        elif(file == 'credentials.json'):
            continue
        else:
            os.rename(file,new_file_name)
            i += 1
