"""
===== Initial Thoughts =====
did this problem with clay. Failed the first one with a dumb but close solution...

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        d = {}
        def build_dict_to_dest(node):
            if node.val == destValue:
                d[node.val] = ""
                return ""
            for child, direction in [(node.left, "L"), (node.right, "R")]:
                s = build_dict_to_dest(node.left)
                if s is not None:
                    val = direction + s
                    d[node.val] = val
                    return val
        
        build_dict_to_dest(root)
        if startValue in d:
            return d[startValue]
        answer = None
        def dfs(node):
            nonlocal answer
            if node.val == startValue:
                return "U"
            for child in [node.left, node.right]:
                if child:
                    s = dfs(child)
                    if s is not None:
                        if node.val in d:
                            answer = s + d[node.val]
                        return s + "U"
            
        dfs(root)
        return answer

then he gave me a hint and I was able to complete it perfectly in 15 minutes
"""

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_str_path(node, target):
            if node.val == target:
                return ""
            for child, direction in [(node.left, "L"), (node.right, "R")]:
                if child:
                    s = find_str_path(child, target)
                    if s is not None:
                        return direction + s
        path_to_start = find_str_path(root, startValue)
        path_to_dest = find_str_path(root, destValue)
        i = 0
        for l, r in zip(path_to_start, path_to_dest):
            if l == r:
                i += 1
            else:
                break
        ups = "U" * (len(path_to_start) - i)
        rest = path_to_dest[i:]
        return ups + rest
