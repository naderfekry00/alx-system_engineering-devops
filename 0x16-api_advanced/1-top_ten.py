#!/usr/bin/python3
"""
top ten hot posts
"""
import requests


def top_ten(subreddit):
    """ function get top ten in reddit"""
    url = ("https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit))
    headers = {
        'User-Agent': 'Python:subreddit.testing.for.alx'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print("None")
