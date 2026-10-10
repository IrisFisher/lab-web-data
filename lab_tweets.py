# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.

import json
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

alltweets = []


def count_tweets(alltweets, word):
    counter = 0
    for j in alltweets:
        try:
            if ((word).lower() in (j['full_text']).lower()):
                counter += 1
        except KeyError:
            try:
                if ((word).lower() in (j['text']).lower()):
                    counter += 1
            except KeyError:
                pass
    print(word + ': ' + str(counter))
    return(counter)

for i in range(2009,2019):
    file = 'master_' + str(i) + '.json'
    with open(file, encoding='utf-8') as f:
        for i in json.load(f):
            alltweets.append(i) #alltweets.append

print('total: ' + str(len(alltweets)))

fake_news = count_tweets(alltweets, 'fake news')
maga = count_tweets(alltweets, 'maga')
mexico = count_tweets(alltweets, 'mexico')
obama = count_tweets(alltweets, 'obama')
russia = count_tweets(alltweets, 'russia')
swamp = count_tweets(alltweets, 'swamp')
trump = count_tweets(alltweets, 'trump')
wall = count_tweets(alltweets, 'wall')

fake_news_percent = fake_news / len(alltweets)
maga_percent = (maga / len(alltweets)) * 100
mexico_percent = (mexico / len(alltweets)) * 100
obama_percent = (obama / len(alltweets)) * 100
russia_percent = (russia / len(alltweets)) * 100
swamp_percent = (swamp / len(alltweets)) * 100
trump_percent = (trump / len(alltweets)) * 100
wall_percent = (wall / len(alltweets)) * 100

x = np.array(["Fake news", "MAGA", "Mexico", "Obama", "Russia", "Swamp", "Trump", "Wall"])
y = np.array([fake_news_percent, maga_percent, mexico_percent, obama_percent, russia_percent, swamp_percent, trump_percent, wall_percent])

print('| phrase            | percent of tweets |\n'
'| ----------------- | ----------------- |\n'
'|         Fake news | ' + str(f'{fake_news_percent:05.2f}') + '             |\n'
'|              MAGA | ' + str(f'{maga_percent:05.2f}') + '             |\n'
'|            Mexico | '+ str(f'{mexico_percent:05.2f}') + '             |\n'
'|             Obama | ' + str(f'{obama_percent:05.2f}') + '             |\n'
'|            Russia | ' + str(f'{russia_percent:05.2f}') + '             |\n'
'|             Swamp | ' + str(f'{swamp_percent:05.2f}') + '             |\n'
'|             Trump | ' + str(f'{trump_percent:05.2f}') + '             |\n'
'|              Wall | ' + str(f'{wall_percent:05.2f}') + '             |\n')

plt.bar(x, y, width =.8)
plt.xlabel('Phrases')
plt.ylabel('Percent of tweets in which phrases appear')
plt.show()
plt.savefig('tweets.png')