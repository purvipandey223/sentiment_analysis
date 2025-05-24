from googleapiclient.discovery import build
import pandas as pd

# Replace with your actual API key and Video ID
API_KEY = 'AIzaSyBcXi8DZbryDW_n2LnWT8FOSjwkLLJCbkI'
VIDEO_ID = 'ovHoY8UBIu8'

# Initialize YouTube API
youtube = build('youtube', 'v3', developerKey=API_KEY)

comments = []
next_page_token = None

while True:
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=VIDEO_ID,
        maxResults=100,
        pageToken=next_page_token,
        textFormat='plainText'
    )
    response = request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

# Save to CSV
df = pd.DataFrame(comments, columns=['comment'])
df.to_csv("youtube_comments.csv", index=False)

print(f"Collected {len(comments)} comments and saved to youtube_comments.csv.")
