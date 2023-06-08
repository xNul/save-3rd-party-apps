# Save 3rd Party Apps

Recently, there has been an uproar over on Reddit because the company has decided to price their public API so high it will render all 3rd party apps which use it, dead. You can learn more about the problem [here](https://www.reddit.com/r/Save3rdPartyApps/comments/13yh0jf/dont_let_reddit_kill_3rd_party_apps/).

There's a growing [list](https://www.reddit.com/r/ModCoord/comments/1401qw5/incomplete_and_growing_list_of_participating/) of subreddits participating in the protest, but it's difficult to gauge the participation across Reddit and what subreddits have yet to decide if they are going to participate. That's where https://save3rdpartyapps.com/ comes in. It shows the top 250 subreddits and their current participation status.

Also, if you know of any subreddits which have decided to not participate in the protest, please add them to the [list](https://github.com/xNul/save-3rd-party-apps/wiki/List-of-Not-Participating-Subreddits). Anyone can edit it as long as they have a GitHub account. Once we get enough subreddits, we can add a red marker to those subreddits on the website.

**Note:** Apparently some people have been harassing the mods of subreddits that have chosen not to take part. *Please do not do this.* It's not helpful to the protest. You can read more about it [here](https://old.reddit.com/r/Save3rdPartyApps/comments/142si7s/do_not_harass_mods_who_have_chosen_not_to_take/).

## Setup

save3rdpartyapps.com is a static website generated from a template and list of participating subreddits. First, we generate the list of subreddits that are participating. Second, we use that list to generate the website from the template.

Steps:
1. Copy and paste the latest participating subreddits from the [list](https://old.reddit.com/r/ModCoord/comments/1401qw5/incomplete_and_growing_list_of_participating/) into `_data/top_part_subs.txt`.
2. Run the `get_part_250_subs.py` script with `python _scripts/get_part_250_subs.py > _data/part_250_subs.txt`. We now have our list of top 250 participating subreddits in `_data/part_250_subs.txt`.
3. Run the `update_part_250_subs.py` script with `python update_part_250_subs.py` which generates `index.html` from our list and `_data/template.html`.

All done!

## Contributing

If anyone wants to clean up the `template.html` or add other features, feel free to submit a PR.
