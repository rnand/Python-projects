import praw
import pprint

# This is an example exercice for PRAW found in https://praw.readthedocs.org/en/v2.1.21/pages/getting_started.html
#This script returns the subreddit-wise breakdown of karma of a user

user_agent ="windows:python_praw_test:v0.1(by /u/d4rk3n3rgy" #sets the useragent 
r=praw.Reddit(user_agent=user_agent) 						 #
user_name=raw_input("Enter the reddit username:")

user=r.get_redditor(user_name)
thing_limit=10                                              #set the request-return limit
gen=user.get_submitted(limit=thing_limit)
karma_by_subreddit={}
for thing in gen:
	subreddit = thing.subreddit.display_name
	karma_by_subreddit[subreddit]=(karma_by_subreddit.get(subreddit,0)+thing.score)

print "The subreddit-wise breakdown of "+user_name+" is:"
pprint.pprint(karma_by_subreddit)
