"""
===== Initial Thoughts =====
This question is sus. I guess they are not always in order with the timestamps?

failed about half of them...

["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
[436363475,710406388,386655081,797150921]
["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]

[386655081, 436363475, 710406388, 797150921]

436363475,710406388,386655081,797150921
386655081,436363475,710406388,797150921
oz, wnaaxbfhxp, mryxsjc - (wlarkzzqht) - my order
["oz","mryxsjc","wlarkzzqht"] - their order

I don't know how their order maskes sense...

Oh, I think I might get it... you can skip ones...

username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], 
timestamp = [1,2,3,4,5,6,7,8,9,10], 
website = ["home","about","career","home","cart","maps","home","home","about","career"]

["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
[527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]

defaultdict(<class 'list'>, {
'h': [(134127993, 'hibympufi'), (527896567, 'hibympufi'), (926837079, 'yljmntrclw')], 
'eiy': [(334462937, 'hibympufi')], 
'cq': [(51100299, 'hibympufi'), (317455832, 'hibympufi'), (411747930, 'yljmntrclw'), (517687281, 'hibympufi'), (859112386, 'hibympufi')], 
'txldsscx': [(159548699, 'hibympufi'), (444082139, 'hibympufi')]})

defaultdict(<class 'int'>, {
'hibympufi-hibympufi-yljmntrclw': 2, 
'hibympufi-hibympufi-hibympufi': 4, 
'hibympufi-yljmntrclw-hibympufi': 4, 
'yljmntrclw-hibympufi-hibympufi': 1})

The thing I'm failing to consider is that a result can only come from a user once.
"""
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        counts, user_visits = defaultdict(int), defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            user_visits[u].append((t, w))
        for user, visits in user_visits.items():
            user_visits[user] = sorted(visits)

        for user, visits in user_visits.items():
            seen = set()
            for i in range(len(visits) - 2):
                for j in range(i + 1, len(visits) - 1):
                    for k in range(j + 1, len(visits)):
                        seq = f"{visits[i][1]}-{visits[j][1]}-{visits[k][1]}"
                        if seq not in seen:
                            seen.add(seq)
                            counts[seq] += 1

        highest = max(counts.values())
        return sorted([k for k, v in counts.items() if v == highest])[0].split("-")
