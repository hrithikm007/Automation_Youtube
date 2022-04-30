
from unicodedata import name
from comments import main
from google_apis import create_service

CLIENT_FILE = 'client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = [
	'https://www.googleapis.com/auth/youtube',
	'https://www.googleapis.com/auth/youtube.force-ssl',
	'https://www.googleapis.com/auth/youtubepartner'
]
def comment(video_id):
    service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

    # video_id = '1EgmwQKOCs4'
    channel_id = 'UCtPEsOhu5dTR1Yply-ds-Kw'

    # Example 1. Post A Comment
    request_body = {
        'snippet': {
            'videoId': video_id,
            'topLevelComment': {
                'snippet': {
                    'textOriginal': "Click on this Link to Join Our Group for Deals like these - bit.ly/37v6dxa"
                }
            }
        }
    }

    response = service.commentThreads().insert(
        part='snippet',
        body=request_body
    ).execute()

    print(response)


if __name__ == "__main__":
    comment()