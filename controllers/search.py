from googleapiclient.discovery import build
from config import api_key
from models.video import Video

youtube = build('youtube', 'v3', developerKey=api_key)

def search_videos_info_by_title(query, numResults):
    try:
        search_response = youtube.search().list(
            q=query,
            part='snippet',
            maxResults=numResults,  # Set the number of results you want to retrieve
            type='video'
        ).execute()

        # Parse and return video URLs
        videos = []
        for item in search_response['items']:
            videoObject = Video()
            videoObject.videoId = item['id']['videoId']
            videoObject.videoTitle = item['snippet']['title']
            videoObject.videoUrl = f'https://www.youtube.com/watch?v={videoObject.videoId}'
            videos.append(videoObject.toJSON())

        return videos

    except Exception as e:
        print(f"An error occurred while searching videos: {e}")
        return []  # Return an empty list or handle the error as appropriate


def search_video_url_by_title(query):
    try:
        search_response = youtube.search().list(
            q=query,
            part='snippet',
            maxResults=1,
            type='video'
        ).execute()

        videoObject = Video()
        # Parse and return video URL
        videoObject.videoId = search_response['items'][0]['id']['videoId']  # Gets id of first item in items array
        videoObject.videoTitle = search_response['items'][0]['snippet']['title']
        videoObject.videoUrl = f'https://www.youtube.com/watch?v={videoObject.videoId}'
        
        return videoObject.toJSON()

    except IndexError:
        print("No video found for the given query.")
        return None
    except Exception as e:
        print(f"An error occurred while searching for a video: {e}")
        return None
