#!/usr/bin/python3
"""
recurstion for hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recursive function """
    headers = {
        'User-Agent': 'Python:subreddit.testing.for.alx'
    }
    url = ("https://www.reddit.com/r/{}/hot.json".format(subreddit))
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        hot_list.extend(post['data']['title'] for post in posts)
        after = data['data'].get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
