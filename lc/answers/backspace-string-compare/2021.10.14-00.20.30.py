def transform(string):
    lst = []
    for i in range(len(string)):
        if string[i] == "#":
            if len(lst): lst.pop()
        else:
            lst.append(string[i])
    return "".join(lst)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return transform(s) == transform(t)