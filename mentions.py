import praw 
import json

# read auth data (client_id, client_secret, and user_agent) from auth.json
def getCoins():
    with open('auth.json', 'r') as fin:
        auth = json.load(fin)

    # create reddit object and login with credentials 
    reddit = praw.Reddit(client_id = auth['client_id'], 
                        client_secret = auth['client_secret'], 
                        user_agent = auth['user_agent'])

    # import list of cryptocurrencies from list.txt and create frequency dict
    with open('list.txt', 'r') as f: 
            coins = [line.rstrip() for line in f]
    freq = {key: 0 for key in coins}

    # gather post data from r/cryptocurrency
    posts = reddit.subreddit('CryptoCurrency').hot(limit = 100)
    postContent = [(post.title + " " + post.selftext )for post in posts]

    # check for mentions and update dict if mentioned
    keys = freq.keys() 
    for key in keys:
        for post in postContent:
            mentions = post.find(key)
            if mentions >= 0:
                freq[key] += mentions

    # remove zero-valued keys and sort by number of mentions  
    freq = {k: v for k, v in freq.items() if v} 
    sortedCoins = sorted(freq.items(), key = lambda x: x[1], reverse=True) 

    # return list of coin-mention pairs 
    return sortedCoins