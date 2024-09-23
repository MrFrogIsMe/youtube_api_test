from googleapiclient.discovery import build

# 你的 YouTube Data API 金鑰
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 建立 YouTube API 客戶端
youtube = build('youtube', 'v3', developerKey=api_key)

# 1. 抓取影片元數據（影片ID範例）
def get_video_metadata(video_id):
    response = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    ).execute()

    for item in response['items']:
        title = item['snippet']['title']
        description = item['snippet']['description']
        view_count = item['statistics']['viewCount']
        like_count = item['statistics'].get('likeCount', 0)

        print(f"標題: {title}")
        print(f"描述: {description}")
        print(f"觀看次數: {view_count}")
        print(f"按讚數: {like_count}")

# 2. 抓取頻道資訊（頻道ID範例）
def get_channel_info(channel_id):
    response = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    ).execute()

    for item in response['items']:
        title = item['snippet']['title']
        subscriber_count = item['statistics']['subscriberCount']
        video_count = item['statistics']['videoCount']

        print(f"頻道名稱: {title}")
        print(f"訂閱者數: {subscriber_count}")
        print(f"影片總數: {video_count}")

# 3. 抓取播放列表及其影片（頻道ID範例）
def get_playlists(channel_id):
    response = youtube.playlists().list(
        part="snippet",
        channelId=channel_id,
        maxResults=5  # 抓取前5個播放列表
    ).execute()

    for playlist in response['items']:
        playlist_id = playlist['id']
        playlist_title = playlist['snippet']['title']
        print(f"播放列表: {playlist_title} (ID: {playlist_id})")

        # 取得播放列表中的影片
        get_playlist_videos(playlist_id)

def get_playlist_videos(playlist_id):
    response = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=5  # 每個播放列表抓取前5部影片
    ).execute()

    for item in response['items']:
        video_title = item['snippet']['title']
        video_id = item['snippet']['resourceId']['videoId']
        print(f" 影片: {video_title} (ID: {video_id})")

# 4. 抓取影片的評論（影片ID範例）
def get_video_comments(video_id):
    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=5  # 抓取前5條評論
    ).execute()

    for comment in response['items']:
        author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
        text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        print(f"作者: {author}")
        print(f"評論: {text}")

# 5. 根據關鍵字搜尋影片
def search_videos_by_keyword(keyword):
    response = youtube.search().list(
        part="snippet",
        q=keyword,
        type="video",
        maxResults=5  # 抓取前5個搜尋結果
    ).execute()

    for item in response['items']:
        video_title = item['snippet']['title']
        video_id = item['id']['videoId']
        print(f"搜尋結果: {video_title} (ID: {video_id})")

# # 6. 抓取訂閱者和頻道的訂閱內容（頻道ID範例）
# def get_channel_subscriptions(channel_id):
#     response = youtube.subscriptions().list(
#         part="snippet",
#         channelId=channel_id,
#         maxResults=5  # 抓取前5個訂閱頻道
#     ).execute()

#     for item in response['items']:
#         subscribed_channel_title = item['snippet']['title']
#         print(f"訂閱頻道: {subscribed_channel_title}")

# 7. 抓取影片的統計數據
def get_video_statistics(video_id):
    response = youtube.videos().list(
        part="statistics",
        id=video_id
    ).execute()

    for item in response['items']:
        view_count = item['statistics']['viewCount']
        like_count = item['statistics'].get('likeCount', 0)
        comment_count = item['statistics'].get('commentCount', 0)

        print(f"觀看次數: {view_count}")
        print(f"按讚數: {like_count}")
        print(f"評論數: {comment_count}")

# 測試資料（替換成你要查詢的資料）
video_id = '14_q4acrt4Y'
channel_id = 'UCbIJeyl_va8MG2xx0q4Uobg'
keyword = '熱門影片'

# 測試各個函數
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


# 好像要用oath2.0 key才可以
# print("\n訂閱頻道:")
# get_channel_subscriptions(channel_id)

print("\n影片的統計數據:")
get_video_statistics(video_id)
