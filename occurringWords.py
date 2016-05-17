# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:11:38 2016

@author: N + S
"""

import json
import re

# Loading tweets and list of English stop words
Tweets = json.loads(open('./input_files/Tweets_Geolocation.json').read())
stop_words = json.loads(open('./input_files/en.json').read())
keywords = dict.fromkeys(['Lesbo', 'Dyke', 'Whore', 'Bitch', 
	'Fag', 'Slut', 'Cunt', 'Faggot', 'Bimbo', 'Fatso', 'Floozy',
	'Poontang', 'Pussy', 'Twat', 'Wussy'])

map_words = {}
for twt in Tweets:
    #print twt['text']
    for wrd in twt['text'].strip().split(' '):
        txt = wrd.strip().split('.')[0]
        if txt != 'https://t' and txt not in stop_words and txt not in keywords:
            map_words[txt] = 1#.strip().split('@')[-1:]
            #print txt (?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)
            
            is_user = re.match( r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)',txt )
            is_hashtag = re.match( r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))#([A-Za-z]+[A-Za-z0-9]+)',txt )
            if  is_user == None and is_hashtag == None:
                print txt


reduce_words = set(map_words)

