import json
import operator
#Reading in the json file with tweets
json_data=open('./input_files/Tweets_Geolocation.json').read()
Tweets = json.loads(json_data)

#users = []
usersset = set()

#names = []
namesset = set()

count = 0
for tweet in Tweets:
	if tweet['entities']['user_mentions']:
		count +=1 
		for user in tweet['entities']['user_mentions']:
			try:

				if str(user['screen_name']) not in usersset:
					#users.append(str(user['screen_name']))
 					usersset.add('@'+str(user['screen_name']))

				if str(user['name']) not in namesset:
					#names.append(str(user['name']))
					namesset.add(str(user['name']))
			except:

				pass

print count
#Initializing a dictionary with keywords used for queries
usernames = dict.fromkeys(usersset)

for k, v in usernames.iteritems():
	if v == None:
		usernames[k] = 0

for key in usernames.iterkeys():
	for tweet in Tweets:
		if tweet['entities']['user_mentions']:
			for user in tweet['entities']['user_mentions']:
				if str(key) == '@'+str(user['screen_name']):
					usernames[key] += 1

realnames = dict.fromkeys(namesset)

for k, v in realnames.iteritems():
	if v == None:
		realnames[k] = 0

for key in realnames.iterkeys():
	for tweet in Tweets:
		if tweet['entities']['user_mentions']:
			for user in tweet['entities']['user_mentions']:
				try:
					if str(key) == str(user['name']):
						realnames[key] += 1
				except:
					pass

print sum(usernames.itervalues())
#print usernames
print sum(realnames.itervalues())
#print realnames

if len(usernames.keys())>10:
    with open('./input_files/twtCount-mentions.json', 'w') as fp:
        json.dump(dict( sorted(usernames.items(), key=operator.itemgetter(1))[-11:]), fp)
else:
    with open('./input_files/twtCount-mentions.json', 'w') as fp:
        json.dump(usernames, fp)