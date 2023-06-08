# List of the Top Participating Subreddits in the Top 250 Largest Subreddits
part_250_subs_file = open("../_data/part_250_subs.txt", "r", encoding="utf-8")
part_250_subs = [line.rstrip() for line in part_250_subs_file]

# Template Top 250 Subreddits HTML Website
template_file_file = open("../_data/template.html", "r", encoding="utf-8")
template_file = template_file_file.read()

# Color codes the subreddits on the list
for subreddit in part_250_subs:
    template_file = template_file.replace("data-prefixed-name=\"" + subreddit + "\"", "data-prefixed-name=\"r/" + subreddit + "\"\n      style=\"background: green\"")

# Write out the resulting HTML website
index_file_file = open("../index.html", "w", encoding="utf-8")
index_file_file.write(template_file)
