#!/usr/bin/python3
"""
recursion for hot articles with keywords
"""
import requests


def count_words(subreddit, word_list):
    """ search function with keywords """
    word_list = [word.lower() for word in word_list]
    new_dic = recursive(subreddit, word_list, None, None)
    if new_dic:
        sorted_dic = sorted(new_dic.items())
        for key, value in sorted_dic:
            if value > 0:
                print("{}: {}".format(key, value))


def recursive(subreddit, word_list, after=None, new_dic=None):
    """ recursive function """
    if new_dic is None:
        new_dic = {word: 0 for word in word_list}
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
        for post in posts:
            title = post['data']['title']
            words_in_title = [word.lower().strip('.,!?:;')
                              for word in title.split()]
            for word in word_list:
                new_dic[word] += words_in_title.count(word)
        after = data['data'].get('after')
        if after:
            return recursive(subreddit, word_list, after, new_dic)
        else:
            return new_dic
    else:
        return new_dic
