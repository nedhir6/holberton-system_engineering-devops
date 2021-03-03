#!/usr/bin/python3
'''titles of the first 10 hot posts listed for a subreddit'''
import requests
def top_ten(subreddit):
    headers = {'User-Agent': 'ned6'}
    res = requests.get(
        'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit),
        headers=headers)
    if res.status_code != 200:
        print(None)
        return
    data = res.json()['data']['children']
    for i in data:
        print(i['data']['title'])
