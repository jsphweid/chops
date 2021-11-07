def get_match_indices(text, word):
    matches = []
    # "foxhouse" "ox"
    for i in range(len(text)):
        if word[0] == text[i]: # first letter matches
            if text[i: i + len(word)] == word:
                matches.append([i, i + len(word) - 1])
    return matches

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        results = []
        for word in words:
            results.extend(get_match_indices(text, word))
        results.sort(key=lambda p: (p[0], p[1]))
        return results