# This Script displays the recent 5 posts of a user in Twitter

import twitter

usrname = raw_input("Enter Twitter User Id or Short Name to display recent 5 tweets : ")

api = twitter.Api()

tweets = api.GetUserTimeline(usrname)

for i in range(5) :
    print "\nTweet(%d) - %s" % (i+1, tweets[i].text)
