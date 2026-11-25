import csv, re, collections
rows = list(csv.DictReader(open('data/saas-directories.csv', encoding='utf-8')))
asof = rows[0]['data_as_of']
SECTIONS = [
 ('AI tool directory', 'AI tools directory list', 'Every AI tools directory we found where you can submit your AI tool, agent or GPT. Each row shows whether listing is free or paid.'),
 ('Launch/startup platform', 'Product Hunt alternatives and startup directories', 'Launch platforms and startup directories where you can launch a new product. Many run daily or weekly launch boards, like Product Hunt.'),
 ('SaaS review/discovery', 'SaaS directories and review sites', 'Software directories and review sites that buyers use to compare SaaS tools.'),
 ('Deals marketplace', 'Deals and lifetime-deal marketplaces', 'Marketplaces that sell discounted or lifetime deals for software.'),
 ('Tools/no-code directory', 'Tools and no-code directories', 'Curated lists of tools, APIs and no-code products.'),
 ('Community', 'Communities', 'Maker communities where you can share what you build.'),
 ('Investor/startup database', 'Investor and startup databases', 'Startup databases used by investors and job seekers.'),
 ('Inspiration/feedback', 'Inspiration and feedback sites', 'Sites that feature new startups or collect feedback.'),
 ('Directory', 'Other directories', 'Directories that do not fit the groups above.'),
]
COST = {'Free': 'Free', 'Paid': 'Paid', 'Unknown': 'Not listed'}
def host(u): return re.sub(r'^https?://(www\.)?', '', u).rstrip('/')
def slug(t): return re.sub(r'[^a-z0-9 -]', '', t.lower()).replace(' ', '-')
by = collections.defaultdict(list)
for r in rows: by[r['type']].append(r)
cost = collections.Counter(r['cost_to_list'] for r in rows)
out = []
out.append('# Awesome AI Tools Directory & SaaS Directories\n')
out.append(f'A free list of **{len(rows)} directory submission sites** for AI tools, SaaS and startups: {len(by["AI tool directory"])} AI tools directories, {len(by["Launch/startup platform"])} startup directories and Product Hunt alternatives, and {len(by["SaaS review/discovery"])} SaaS directories. Each entry shows the type of site and whether listing is free or paid.\n')
out.append(f'{cost["Free"]} list for free, {cost["Paid"]} charge to list, and {cost["Unknown"]} do not state a price. Data as of {asof}.\n')
out.append('- **Spreadsheet:** [`data/saas-directories.csv`](data/saas-directories.csv) (name, link, type, cost to list, date)')
out.append('- **Web version:** [indietorch.com/saas-directories](https://indietorch.com/saas-directories)')
out.append('- **Launching a product?** List it free on [Indie Torch](https://indietorch.com), the weekly launch platform that maintains this list.\n')
out.append('> Costs are as each directory reports them. Prices and free tiers change often, so check the submit page before you pay.\n')
out.append('## Contents\n')
for key, title, _ in SECTIONS:
    if by[key]: out.append(f'- [{title}](#{slug(title)}) ({len(by[key])})')
out += ['- [Directories for backlinks: what actually helps](#directories-for-backlinks-what-actually-helps)', '- [How to use this list](#how-to-use-this-list)', '- [Contributing](#contributing)', '- [License](#license)\n']
for key, title, desc in SECTIONS:
    items = by[key]
    if not items: continue
    out.append(f'## {title}\n')
    out.append(f'{desc}\n')
    out.append('| Directory | Website | Cost to list |')
    out.append('| --- | --- | --- |')
    for r in items:
        name = r['name'].replace('|', '/')
        note = ' (maintainer\'s own platform)' if host(r['link']) == 'indietorch.com' else ''
        out.append(f'| [{name}]({r["link"]}){note} | {host(r["link"])} | {COST.get(r["cost_to_list"], r["cost_to_list"])} |')
    out.append('\n**[Back to top](#awesome-ai-tools-directory--saas-directories)**\n')
out.append('''## Directories for backlinks: what actually helps

Directory listings are useful for discovery and referral traffic first, backlinks second.

- **Relevance beats volume.** A listing on an AI tools directory or a SaaS directory in your niche is worth more than hundreds of generic web directories.
- **Many links are nofollow.** Plenty of directories mark outbound links as `nofollow` or `ugc`. They still send visitors, but they pass little ranking value.
- **Avoid link farms.** Sites that accept any URL instantly, or exist only to sell backlinks, can hurt more than help.
- **Paid listings:** if you pay for a listing, the link should be marked `sponsored` under Google's link spam policy.

''')
out.append('''## How to use this list

1. **Start with launch platforms.** They send the most early users. Pick 5 to 10 that match your audience rather than submitting everywhere at once.
2. **Prepare your assets once.** A one-line tagline, a 160-character description, a logo (square PNG), 3 to 5 screenshots and your pricing. Most submit forms ask for the same fields.
3. **List on review sites after launch.** SaaS review and discovery sites matter more once you have customers who can leave reviews.
4. **Use the AI tools directory list only if your product uses AI.** Many are low quality; prefer the ones with a real submit page and visible traffic.
5. **Track where you submitted.** Keep a column for date submitted, status and the live listing URL.

## Contributing

Know an AI tools directory or SaaS directory that is missing, closed or now paid? Open an issue or a pull request that edits [`data/saas-directories.csv`](data/saas-directories.csv). See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC0 1.0](LICENSE). Use the list for anything.

Maintained by [Indie Torch](https://indietorch.com), a weekly launch platform for indie makers.
''')
open('README.md', 'w', encoding='utf-8').write('\n'.join(out))
print(len(out), 'lines')
