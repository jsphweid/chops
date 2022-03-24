"""
===== Initial Thoughts =====
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
5 wiki.org
5 org
1 intel.mail.com
901 mail.com
951 com
50 yahoo.com
900 google.mail.com

=== Implemented Approach ===
use dictionary where the keys are various subdomains/domains 
and the values are the counts

~~Complexity Analysis
Time - O(n)
Space - O(n)

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
num=900, subdomain="google.mail.com" parts=["google", "mail", "com"]
keys=["com", "mail.com", "google.mail.com"]
{"com": 951, "mail.com": 900, "google.mail.com": 900}
"""
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomains_to_counts = defaultdict(int)
        for cpdomain in cpdomains:
            num, subdomain = cpdomain.split(" ")
            num = int(num)
            parts = subdomain.split(".")  # will be either 2 or 3 parts
            keys = [parts[-1], ".".join(parts[-2:])]
            if len(parts) == 3:
                keys.append(subdomain)
            for key in keys:
                subdomains_to_counts[key] += num
        return [f"{c} {s}" for s, c in subdomains_to_counts.items()]