"""
===== Initial Thoughts =====
dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext
tab indicates child

looking for files, not folders

make a graph would be easy to reason about but probably not the fastest..
let's do that for now

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

[dir, \tsubdir1, \t\tfile1.ext, \t\tsubsubdir1, \tsubdir2, \t\tsubsubdir2, \t\t\tfile2.ext]
{0: "dir", 1: "subdir2", 2: "subsubdir2"}
{"dir": ["subdir1"], "subdir1": ["file1.ext"], "subdir2": ["subsubdir2"], "subsubdir2": "file2.ext"}

"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
["dir", "\tsubdir1", "\tsubdir2", "\t\tfile.ext"]
adj={"dir":["subdir1", "subdir2"], "subdir2":["file.ext"]}
curr_tree = {0: "dir", 1: "subdir2"}
root = "dir"

"a\n\taa\n\t\taaa\n\t\t\tfile1234567890123.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png"
"""
from collections import defaultdict
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if "." in input and "\t" not in input:
            return max(map(len, input.split("\n")))

        adj = defaultdict(list)
        sections = input.split("\n")
        curr_tree = {}
        roots = []
        for item in sections:
            num_tabs = item.count("\t")
            name = item.split("\t")[-1]
            if "." not in name:
                curr_tree[num_tabs] = name
            if num_tabs:
                adj[curr_tree[num_tabs - 1]].append(name)
            else:
                roots.append(name)
        longest, seen = 0, set()

        def dfs(node, path):
            if node in seen:
                return
            seen.add(node)
            nonlocal longest
            for child in adj[node]:
                if "." in child:
                    longest = max(longest, sum(map(len, path)) + len(path) + len(child))
                else:
                    dfs(child, path + [child])

        for root in roots:
            dfs(root, [root])
        return longest


