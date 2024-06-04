#!/usr/bin/python3
"""
number of reddit sbscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ function for num of subscribers in reddit"""
    url = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {
        'User-Agent': 'Python:subreddit.testing.for.alx'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
