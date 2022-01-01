"""
===== Initial Thoughts =====
/home/
["home"]

"/home//foo/"
"home foo"

"/home//foo/.././"
"home", "foo" ".." "."

/../Users/joseph.weidinger
"Users" ".."  "joseph.weidinger"
["joseph.weidinger"]
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        discard = {"", "."}
        tokens = [p for p in path.split("/") if p not in discard]
        temp = []
        for token in tokens:
            if token == "..":
                if temp:
                    temp.pop()
            else:
                temp.append(token)
        return f"/{'/'.join(temp)}" if temp else "/"

