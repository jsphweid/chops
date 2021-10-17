"""
["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
we need to group by contents "abcd" "efgh" etc....
but the strings are in a minimal representation, so we need to expand it first

strings are formatted "dir filename(filecontents) filename(filecontents)"
so we can split on " "... index 0 is always dir, the others are files
"""
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            splitted = path.split(" ")
            directory = splitted[0]
            files = splitted[1:]
            for file in files:
                f, contents = file.split("(")
                contents = contents.replace(")", "")
                d[contents].append(f"{directory}/{f}")
        return [v for v in d.values() if len(v) > 1]