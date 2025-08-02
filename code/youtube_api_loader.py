
from googleapiclient.discovery import build
import pandas as pd

# Replace with your API key
API_KEY = "AIzaSyA4FELpXJzOCbbJaQ2RjKHkog_h0lJGEPY"

youtube = build("youtube", "v3", developerKey=API_KEY)

# Call API to get trending videos in India
request = youtube.videos().list(
    part="snippet,statistics,contentDetails",
    chart="mostPopular",
    regionCode="IN",
    maxResults=50
)
response = request.execute()

# Extract and flatten data
records = []
for item in response["items"]:
    record = {
        "videoId": item["id"],
        "title": item["snippet"]["title"],
        "channelTitle": item["snippet"]["channelTitle"],
        "categoryId": item["snippet"]["categoryId"],
        "publishedAt": item["snippet"]["publishedAt"],
        "viewCount": item["statistics"].get("viewCount"),
        "likeCount": item["statistics"].get("likeCount"),
        "commentCount": item["statistics"].get("commentCount"),
        "duration": item["contentDetails"].get("duration"),
    }
    records.append(record)

# Convert to DataFrame and save
df = pd.DataFrame(records)
df.to_csv("data/youtube_api_sample.csv", index=False)
print("Saved trending videos to data/youtube_api_sample.csv")
