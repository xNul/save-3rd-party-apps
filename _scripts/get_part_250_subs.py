# List of Top Participating Subreddits
top_part_subs_file = open("../_data/top_part_subs.txt", "r")
top_part_subs = [line.rstrip().lower() for line in top_part_subs_file]
top_part_subs = [line for line in top_part_subs if line.startswith("r/")]

# List of Top 250 Largest Subreddits
top_250_file = open("../_data/top_250.txt", "r")
top_250 = [line.rstrip().lower() for line in top_250_file]

# List of Top 250 Latest Subreddits with original names
top_250_file = open("../_data/top_250.txt", "r")
top_250_notlower = [line.rstrip() for line in top_250_file]

# Output file for the list of the Top Participating Subreddits in the Top 250 Largest Subreddits
part_250_subs_file = open("../_data/part_250_subs.txt", "w")

# List the Top Participating Subreddits in the Top 250 Largest Subreddits
for i, subreddit in enumerate(top_250):
	if subreddit in top_part_subs:
		part_250_subs_file.write(top_250_notlower[i] + "\n")
