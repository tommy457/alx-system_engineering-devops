#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API,
    returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {'User-Agent': 'Firefox/120.0'}

    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        data = res.json().get("data")
        return data.get("subscribers")
    return 0
