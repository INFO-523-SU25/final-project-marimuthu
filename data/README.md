# Dataset - 1:
## YouTube Trending Video Dataset (Kaggle – India)
   - This data set contains trending YouTube videos in India along with engagement metrics.

# Codebook for YouTube Trending Video Dataset in India

## Variable Names and Descriptions:

- `video_id`: Unique ID for the video
- `title`: Title of the video
- `publishedAt`: Date and time the video was published
- `channelId`: Unique ID for the channel
- `channel_title`: Name of the channel
- `categoryid`: Category code (numerical)
- `trending_date`: Date when the video was trending
- `tags`: List of tags associated with the video
- `view_count`: Number of views
- `likes`: Number of likes
- `dislikes`: Number of dislikes
- `comment_count`: Number of comments
- `thumbnail_link`: URL to thumbnail image
- `comments_disabled`: Whether comments are disabled
- `ratings_disabled`: Whether ratings are disabled
- `description`: Full text description of the video

## Data Types:

- `video_id`: object
- `title`: object
- `publishedAt`: object
- `channelId`: object
- `channel_title`: object
- `categoryid`: numeric
- `trending_date`: object
- `tags`: object
- `view_count`: numeric
- `likes`: numeric
- `dislikes`: numeric
- `comment_count`: numeric
- `thumbnail_link`: object
- `comments_disabled`: boolean
- `ratings_disabled`: boolean
- `description`: object

---

## Dataset - 2
## 1000 Most Trending YouTube Videos (Kaggle)
- This dataset contains the 1,000 most trending YouTube videos globally, including engagement metrics and video metadata.

# Codebook for YouTube International Trending Video Dataset

## Variable Names and Descriptions:

- `rank`: Rank of video in the trending list
- `Video`: Title of the video
- `Video views`: Number of views
- `Likes`: Number of likes
- `Dislikes`: Number of dislikes
- `Category`: Category of the video
- `published`: Year the video was published

## Data Types:

- `rank`: numeric
- `Video`: object
- `Video views`: object
- `Likes`: object
- `Dislikes`: object
- `Category`: object
- `published`: numeric

# Dataset - 3
## YouTube Trending Videos via API (India)
- This dataset contains trending YouTube videos in India fetched using the YouTube Data API, including engagement metrics and metadata for the most popular recent videos.

# Codebook for YouTube Trending Video Dataset

## Variable Names and Descriptions:

- `videoId`: Unique ID for the video
- `title`: Title of the video
- `channelTitle`: Title of the channel
- `categoryId`: Category code (numerical)
- `publishedAt`: Date and time the video was published
- `viewCount`: Number of views
- `likeCount`: Number of likes
- `commentCount`: Number of comments
- `duration`: Length of the video (in ISO 8601 duration format)

## Data Types:

- `videoId`: object
- `title`: object
- `channelTitle`: object
- `categoryId`: numeric
- `publishedAt`: object
- `viewCount`: numeric
- `likeCount`: numeric
- `commentCount`: numeric
- `duration`: object



