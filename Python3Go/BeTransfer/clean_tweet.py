#4. Clean up the following tweet so that it contains only the user’s message.
# That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

tweet = '''
#man Good advice! RT @TheNextWeb: What I would do differently if I 
was learning to code today  http://t.co/lbwej0pxOd cc: @garybernhardt #rstats  
'''

#tweet=input("Enter a text randomly: ")
#desired_output = 'Good advice What I would do differently if I was learning to code today'

import re
def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)  # remove URLs
    tweet = re.sub('RT|cc', '', tweet)  # remove RT and cc
    tweet = re.sub('#\S+', '', tweet)  # remove hashtags
    tweet = re.sub('@\S+', '', tweet)  # remove mentions
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
    tweet = re.sub('\s+', ' ', tweet)  # remove extra whitespace
    return tweet

print(clean_tweet(tweet))
