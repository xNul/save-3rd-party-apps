import time
import praw

# Reddit API information goes here
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

# List of the Top 250 Largest Subreddits
top_250_file = open("../_data/top_250.txt", "r")
top_250 = [line.rstrip()[2:] for line in top_250_file]

# Find all mods which are reddit admins in the Top 250 Largest Subreddits
for subreddit in top_250:
    print(subreddit)
    for moderator in reddit.subreddit(subreddit).moderator():
        if hasattr(moderator, "is_employee") and moderator.is_employee:
            print(subreddit + ": " + moderator.name)
            break
