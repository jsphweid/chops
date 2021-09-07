"""
0,1  1,0
0,2  2,0
0,3  3,0

1,2  2,1
1,3  3,1

2,3  3,2

that is 12/16... but the other 4 (diagonal are irrelevant)
"""

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        num_words = len(words)
        max_word_length = max([len(w) for w in words])
        if num_words != max_word_length:
            return False
        padded_words = [w + ("x" * (max_word_length - len(w))) for w in words]

        for i in range(num_words - 1):
            for j in range(i + 1, num_words):
                if padded_words[i][j] != padded_words[j][i]:
                    return False
        return True