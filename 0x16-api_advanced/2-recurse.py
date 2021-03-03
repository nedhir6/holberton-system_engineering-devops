#!/usr/bin/python3
'''recurse'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    headers = {'User-Agent': 'ned6'}
    res = requests.get(
        'https://www.reddit.com/r/{}/hot.json?after={}'.
        format(subreddit, after), headers=headers)
    if res.status_code != 200:
        return None
    info = res.json()
    data1 = info.get('data')
    chi = data1.get('children')
    for i in chi:
        hot_list.append(i.get('data').get('title'))
    after = data1.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
