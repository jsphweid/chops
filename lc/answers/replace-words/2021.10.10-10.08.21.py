"""
===== Initial Thoughts =====
hmm, brute force is expensive here

=== Brute Force Approach ===
for each word in the sentence, filter items from dict that can match the word, sort that, return smallest
hmm... if we sort first, I think the first item we find in the dict will be the smallest

i failed once because 

Input:
["a","b","c"]
"aadsfasf absbs bbab cadsfafs"
Output:
"a a a a"
Expected:
"a a b c"

I thought mistakenly it was because I ordered the dictionary and leaned to heavily on that, but actually
it is a fundamental algorithm error. a is NOT an acceptable replacement to `bbab`. The whole `root in word`
business doesn't work here.
"""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        ret_list = []
        for word in sentence.split(" "):
            ret_list.append(word)
            for dict_word in dictionary:
                if word.startswith(dict_word):
                    ret_list.pop()
                    ret_list.append(dict_word)
                    break

        return " ".join(ret_list)
