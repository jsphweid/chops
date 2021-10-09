"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""
import re
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            left, right = email.split("@")
            new_left = re.sub(r"\.|\+.*", "", left)
            s.add(new_left + "@" + right)
        return len(s)