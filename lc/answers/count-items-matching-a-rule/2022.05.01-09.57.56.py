"""
===== Initial Thoughts =====
just filter

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item_type, item_color, item_name in items:
            if ruleKey == "type":
                count += item_type == ruleValue
            if ruleKey == "color":
                count += item_color == ruleValue
            if ruleKey == "name":
                count += item_name == ruleValue
        return count