# Contributing

Thanks for helping keep this list accurate.

## Add, fix or remove a directory

1. Edit [`data/saas-directories.csv`](data/saas-directories.csv). Keep the columns: `name,link,type,cost_to_list,data_as_of`.
2. Use one of these types: `Launch/startup platform`, `SaaS review/discovery`, `AI tool directory`, `Deals marketplace`, `Tools/no-code directory`, `Community`, `Investor/startup database`, `Inspiration/feedback`, `Directory`.
3. Set `cost_to_list` to `Free`, `Paid` or `Unknown`, as the directory states it on its own submit or pricing page.
4. Set `data_as_of` to the date you checked (YYYY-MM-DD).
5. Regenerate the README: `python3 scripts/build_readme.py`.
6. Open a pull request with one directory per line change and a link to its submit page.

## What gets accepted

- The site lists software, startups or AI tools and accepts submissions from makers.
- The site is live and loads without a login wall.
- No link farms, PBNs or sites that only sell backlinks.

## Report a dead or changed link

Open an issue with the directory name and what changed (closed, now paid, new submit URL).
