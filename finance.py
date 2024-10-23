from googleapiclient.discovery import build

API_KEY = 'key'

def search_youtube_videos(query, max_results=5):
    # Build the YouTube API service
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Call the search.list method to retrieve videos
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results
    ).execute()

    # Extract video information from the response
    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video = {
                'title': search_result['snippet']['title'],
                'video_id': search_result['id']['videoId'],
                'thumbnail': search_result['snippet']['thumbnails']['default']['url'],
                'description': search_result['snippet']['description']
            }
            videos.append(video)
    return videos
