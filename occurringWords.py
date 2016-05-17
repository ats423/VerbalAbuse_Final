# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:11:38 2016

@author: N + S
"""

import json

# Loading tweets and list of English stop words
Tweets = json.loads(open('./input_files/Tweets_Geolocation.json').read())
stop_words = json.loads(open('./input_files/en.json').read())


map_words = {}
for twt in Tweets:
    #print twt['text']
    for wrd in twt['text'].strip().split(' '):
        txt = wrd.strip().split('.')[0]
        if txt != 'https://t' and txt not in stop_words:
            map_words[txt] = 1#.strip().split('@')[-1:]


reduce_words = set(map_words)

