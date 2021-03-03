#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'ned6'}
    res = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=headers)
    if res.status_code != 200:
        return 0
    info = res.json()
    return(info.get('data').get('subscribers'))
