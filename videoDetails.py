import os
from googleapiclient.http import MediaFileUpload

class Video:
    description = "Amazon Flipkart Myntra Ajio & ManyJoin Our Telegram Channel For Great Shopping Deals - https://telegram.im/@zabardastdeals #HRITHIK007,#shopping,#zabardastdeals"
    category = "22"
    keywords = "test"
    privacyStatus = "public"

    def getFileName(self, type):
        for file in os.listdir("Downloaded Reels/"):
            if type == "video" and file.split(".", 1)[1] != "jpg":
                return file
                break
            elif type == "thumbnail" and file.split(".", 1)[1] != "mp4":
                return file
                break

    def insertThumbnail(self, youtube, videoId):
        thumnailPath = "Downloaded Reels/%s" % (self.getFileName("thumbnail"))

        request = youtube.thumbnails().set(
            videoId=videoId,
            media_body=MediaFileUpload(thumnailPath)
        )
        response = request.execute()
        print(response)