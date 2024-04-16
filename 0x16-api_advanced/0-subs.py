#!/usr/bin/python3
"""Func that queries Reddit API, returns no. of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Returns n0. of subscribers for a given subreddit"""
    URL = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "My Reddit API Script 0.1"}
    response = requests.get(URL, headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json()
    subscribers = results.get('data', {}).get('subscribers', 0)
    return subscribers
