
from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        def get_uniques(sentence):
            ret = set()
            ignore = set()
            for word in sentence.split(" "):
                if word not in ret and word not in ignore:
                    ret.add(word)
                elif word in ret:
                    ret.remove(word)
                    ignore.add(word)
            return ret, ignore
        s1_uniques, s1_ignores = get_uniques(s1)
        s2_uniques, s2_ignores = get_uniques(s2)
        return (s1_uniques ^ s2_uniques) - s1_ignores - s2_ignores
