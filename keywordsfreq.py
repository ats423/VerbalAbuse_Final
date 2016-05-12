import json

#Reading in the json file with tweets
json_data=open('Day1_Tweets.json').read()
Tweets = json.loads(json_data)

#Initializing a dictionary with keywords used for queries
keywords = dict.fromkeys(['Lesbo', 'Dyke', 'Whore', 'Bitch', 
	'Fag', 'Slut', 'Cunt', 'Faggot', 'Bimbo', 'Fatso', 'Floozy',
	'Poontang', 'Pussy', 'Twat', 'Wussy'])

for k, v in keywords.iteritems():
	if v == None:
		keywords[k] = 0

#print len(Tweets)

for tweet in Tweets:
	for k, v in keywords.iteritems():
		if k.lower() in tweet['text'].encode('utf-8').lower():
			keywords[k] += 1

#print keywords
