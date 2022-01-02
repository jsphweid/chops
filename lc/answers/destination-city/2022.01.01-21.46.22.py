class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dest = set(), set()
        for left, right in paths:
            src.add(left)
            dest.add(right)
        return list(dest - src)[0]