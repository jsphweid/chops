"""
[1,3,4]
["Push", "Push", "Pop"]
"""

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 1
        for num in target:
            if i != num:
                res.extend(["Push", "Pop"] * (num - i))
                i = num
            res.append("Push")
            i += 1
        return res
