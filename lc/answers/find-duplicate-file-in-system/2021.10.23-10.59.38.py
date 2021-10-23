from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for path in paths:
            directory, *files = path.split(" ")
            for file in files:
                filename, content = file.split("(")
                content = content.replace(")", "")
                m[content].append(f"{directory}/{filename}")
        return [d for d in m.values() if len(d) > 1]