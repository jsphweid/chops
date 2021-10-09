"""
===== Initial Thoughts =====
let's use regex

=== Brute Force Approach ===
create a new empty string
iterate over each char adding the char to the empty string... but if it's a `.` add `[.]` to the string

=== Implemented Approach ===
use regex

~~Complexity Analysis
Time - 
Space - 
"""
import re
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub("\.", "[.]", address)