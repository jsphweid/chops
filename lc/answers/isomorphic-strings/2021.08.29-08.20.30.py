class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        already_used = set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in already_used:
                    return False
                mapping[s[i]] = t[i]
                already_used.add(t[i])
        return True
    """
    failed first time because I didn't understand the problem, it's not a strict two way mapping
    failed again because I mistakenly "simplified an `if` statement" that couldn't have been 
    simplified like that. Additionally, I'd like to come back to this at some point in the near 
    future
    """