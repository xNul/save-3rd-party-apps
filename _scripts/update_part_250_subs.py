# List of the Top Participating Subreddits in the Top 250 Largest Subreddits
part_250_subs_file = open("../_data/part_250_subs.txt", "r", encoding="utf-8")
part_250_subs = [line.rstrip() for line in part_250_subs_file]
part_250_subs = [(subreddit, "participating") for subreddit in part_250_subs]

# List of the Top 250 Largest Subreddits which have an admin as a mod
top_250_with_admin_file = open("../_data/top_250_with_admin_mod.txt", "r", encoding="utf-8")
top_250_with_admin = [line.rstrip() for line in top_250_with_admin_file]
top_250_with_admin = [(subreddit, "hasadmin") for subreddit in top_250_with_admin]

combined_changes = part_250_subs# + top_250_with_admin

# Template Top 250 Subreddits HTML Website
template_file_file = open("../_data/template.html", "r", encoding="utf-8")
template_file = template_file_file.read()

# Color codes the subreddits on the list
for subreddit, new_class in combined_changes:
    template_file = template_file.replace("data-prefixed-name=\"" + subreddit + "\"", "data-prefixed-name=\"" + subreddit + "\"\n      class=\"flex flex-wrap justify-center py-[0.75rem] " + new_class + "\"")

# Adds the fraction of subreddits which are participating
template_file = template_file.replace("{{GOING_DARK_FRACTION}}", "(" + str(len(part_250_subs)) + "/250)")

# Write out the resulting HTML website
index_file_file = open("../index.html", "w", encoding="utf-8")
index_file_file.write(template_file)
