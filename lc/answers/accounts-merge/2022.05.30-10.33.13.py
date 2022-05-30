"""
===== Initial Thoughts =====
[
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
[
    ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]

John|johnsmith@mail.com -> 0
John|john_newyork@mail.com -> 0
John|johnsmith@mail.com -> 1
John|john00@mail.com -> 1

[0 0 2 3]

[
    ["John"]
]

John|john00@mail.com -> 0   -> IS 0
John|johnsmith@mail.com -> 1   -> IS 1
John|john_newyork@mail.com -> 1
John|johnsmith@mail.com -> 2   -> IS 1
John|john00@mail.com -> 3


--------

[
    ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
    ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
    ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
    ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
    ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
[
    ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
    ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
    ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
    ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
    ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]

=== Implemented Approach ===
union find but it's hard

let's try brute force

nah, we gotta do uf

~~Complexity Analysis
Time - 
Space - 

[
    ["David","David0@m.co","David1@m.co"]
    ["David","David3@m.co","David4@m.co"]
    ["David","David4@m.co","David5@m.co"]
    ["David","David2@m.co","David3@m.co"]
    ["David","David1@m.co","David2@m.co"]
]

1 1 1 1 0

"0": 0   "1": 0    "3": 1    "4": 1    "2": 3
find(2) = find(1)
find(3) = find(1)
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = list(range(len(accounts)))
        key_to_i = {}

        def find(i):
            if uf[i] == i:
                return i
            uf[i] = find(uf[i])
            return uf[i]

        for i, account in enumerate(accounts):
            name, *emails = account
            for email in emails:
                key = f"{name}|{email}"
                if key in key_to_i:
                    uf[find(i)] = find(key_to_i[key])
                else:
                    key_to_i[key] = find(i)

        sets = [set() for _ in range(len(accounts))]
        for i, account in enumerate(accounts):
            name, *emails = account
            keys = {f"{name}|{email}" for email in emails}
            sets[uf[find(i)]] |= keys

        res = []
        for s in sets:
            if s:
                lst = list(s)
                name = lst[0].split("|")[0]
                emails = [key.split("|")[1] for key in lst]
                emails.sort()
                res.append([name] + emails)
        return res




