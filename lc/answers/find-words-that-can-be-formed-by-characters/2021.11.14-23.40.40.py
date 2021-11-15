from collections import defaultdict

def make_count_dict(string: str):
    res = defaultdict(int)
    for char in string:
        res[char] += 1
    return res


def is_subset(candidate, truth):
    for char, count in candidate.items():
        if char not in truth or truth[char] < candidate[char]:
            return False    
    return True


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counts = make_count_dict(chars)
        total = 0
        for word in words:
            d = make_count_dict(word)
            if is_subset(d, char_counts):
                total += len(word)
        return total