# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

video_id = 'jOcaG4eLYg0'
channel_id = 'UCtPEsOhu5dTR1Yply-ds-Kw'

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    request2 = youtube.videos().rate(
        id=video_id,
        rating="like"
    )
    request2.execute()

    request = youtube.commentThreads().insert(
        part="snippet",
        body={
          "snippet": {
            "videoId": video_id,
            "topLevelComment": {
              "snippet": {
                "textOriginal": "Click on this Link to Join Our Group for Deals like these - bit.ly/37v6dxa"
              }
            }
          }
        }
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()