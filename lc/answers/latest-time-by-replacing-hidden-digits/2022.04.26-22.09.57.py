class Solution:
    def maximumTime(self, time: str) -> str:
        lst = list(time)
        if lst[0] == "?": lst[0] = "2" if lst[1] == "?" or int(lst[1]) < 4 else "1"
        if lst[1] == "?": lst[1] = "3" if lst[0] == "2" else "9"
        if lst[3] == "?": lst[3] = "5"
        if lst[4] == "?": lst[4] = "9"
        return "".join(lst)