from collections import defaultdict
import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # build map that has contents mapped to filename list
        d = defaultdict(list)

        # parse each entry into dir and filename/contents
        for p in paths:
            splitted = p.split(" ")
            base_dir = splitted[0]
            filename_contents = splitted[1:]
            for fc in filename_contents:
                filename, contents = re.findall(r"\w*\.\w+|(?<=\()\w+(?=\))", fc)
                d[contents].append(f"{base_dir}/{filename}")

        return [v for v in d.values() if len(v) > 1]