# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:11:38 2016

@author: N + S
"""

import json
import re

# Loading tweets and list of English stop words
Tweets = json.loads(open('./input_files/Coordinates_15Keywords_Works.json').read())
stop_words = json.loads(open('./input_files/en.json').read())
keywords = dict.fromkeys(['Lesbo', 'Dyke', 'Whore', 'Bitch', 
	'Fag', 'Slut', 'Cunt', 'Faggot', 'Bimbo', 'Fatso', 'Floozy',
	'Poontang', 'Pussy', 'Twat', 'Wussy'])

map_words = {}
for twt in Tweets:
    #print twt['text']
    for wrd in twt['text'].strip().split(' '):
        txt = wrd.strip().split('.')[0]
        if txt.lower() != 'https://t' and txt.lower() not in stop_words and txt.lower() not in keywords:
            #.strip().split('@')[-1:]
            #print txt (?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)
            
            is_user = re.match( r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)',txt )
            is_hashtag = re.match( r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))#([A-Za-z]+[A-Za-z0-9]+)',txt )
            if  is_user == None and is_hashtag == None:
                try:
                    map_words[txt] += 1
                except KeyError:
                    map_words[txt] = 1

map_words.keys()

import operator

with open('./input_files/twtCount-words.json', 'w') as fp:
   json.dump(dict( sorted(map_words.items(), key=operator.itemgetter(1))[-11:]), fp) 