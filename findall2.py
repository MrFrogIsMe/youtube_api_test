import requests

# Your YouTube Data API key
api_key = 'AIzaSyDE7cnRgBlTJkgoDqjrnDRUCAsc3VAOA2o'

# Base URL for YouTube Data API v3
base_url = 'https://www.googleapis.com/youtube/v3'

# 1. Get video metadata
def get_video_metadata(video_id):
    url = f"{base_url}/videos?part=snippet,statistics&id={video_id}&key={api_key}"
    # print(f"URL: {url}")
    response = requests.get(url)
    data = response.json()

    for item in data.get('items', []):
        title = item['snippet']['title']
        description = item['snippet']['description']
        view_count = item['statistics']['viewCount']
        like_count = item['statistics'].get('likeCount', 0)

        print(f"標題: {title}")
        print(f"描述: {description}")
        print(f"觀看次數: {view_count}")
        print(f"按讚數: {like_count}")

# 2. Get channel info
def get_channel_info(channel_id):
    url = f"{base_url}/channels?part=snippet,statistics&id={channel_id}&key={api_key}"
    # print(f"URL: {url}")
    response = requests.get(url)
    data = response.json()

    for item in data.get('items', []):
        title = item['snippet']['title']
        subscriber_count = item['statistics']['subscriberCount']
        video_count = item['statistics']['videoCount']

        print(f"頻道名稱: {title}")
        print(f"訂閱者數: {subscriber_count}")
        print(f"影片總數: {video_count}")

# 3. Get playlists and their videos
def get_playlists(channel_id):
    url = f"{base_url}/playlists?part=snippet&channelId={channel_id}&maxResults=5&key={api_key}"
    # print(f"URL: {url}")
    response = requests.get(url)
    data = response.json()

    for playlist in data.get('items', []):
        playlist_id = playlist['id']
        playlist_title = playlist['snippet']['title']
        print(f"播放列表: {playlist_title} (ID: {playlist_id})")

        # Get videos in the playlist
        get_playlist_videos(playlist_id)

def get_playlist_videos(playlist_id):
    url = f"{base_url}/playlistItems?part=snippet&playlistId={playlist_id}&maxResults=5&key={api_key}"
    # print(f"URL: {url}")
    response = requests.get(url)
    data = response.json()

    for item in data.get('items', []):
        video_title = item['snippet']['title']
        video_id = item['snippet']['resourceId']['videoId']
        print(f" 影片: {video_title} (ID: {video_id})")

# 4. Get video comments
def get_video_comments(video_id):
    url = f"{base_url}/commentThreads?part=snippet&videoId={video_id}&maxResults=5&key={api_key}"
    # print(f"URL: {url}")
    response = requests.get(url)
    data = response.json()

    for comment in data.get('items', []):
        author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
        text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        print(f"作者: {author}")
        print(f"評論: {text}")

# 5. Search videos by keyword
def search_videos_by_keyword(keyword):
    url = f"{base_url}/search?part=snippet&q={keyword}&type=video&maxResults=5&key={api_key}"
    # print(f"URL: {url}")
    response = requests.get(url)
    data = response.json()

    for item in data.get('items', []):
        video_title = item['snippet']['title']
        video_id = item['id']['videoId']
        print(f"搜尋結果: {video_title} (ID: {video_id})")

# 7. Get video statistics
def get_video_statistics(video_id):
    url = f"{base_url}/videos?part=statistics&id={video_id}&key={api_key}"
    # print(f"URL: {url}")
    response = requests.get(url)
    data = response.json()

    for item in data.get('items', []):
        view_count = item['statistics']['viewCount']
        like_count = item['statistics'].get('likeCount', 0)
        comment_count = item['statistics'].get('commentCount', 0)

        print(f"觀看次數: {view_count}")
        print(f"按讚數: {like_count}")
        print(f"評論數: {comment_count}")

# Test data (replace with your query data)
video_id = '14_q4acrt4Y'
channel_id = 'UCbIJeyl_va8MG2xx0q4Uobg'
keyword = '熱門影片'

# Test each function
print("\n影片元數據:")
get_video_metadata(video_id)

print("\n頻道資訊:")
get_channel_info(channel_id)

print("\n播放列表及其影片:")
get_playlists(channel_id)

print("\n影片的評論:")
get_video_comments(video_id)

print("\n根據關鍵字搜尋影片:")
search_videos_by_keyword(keyword)

print("\n影片的統計數據:")
get_video_statistics(video_id)