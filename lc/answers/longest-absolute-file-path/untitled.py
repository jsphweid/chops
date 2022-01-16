def lengthLongestPath(self, input: str) -> int:
    adj = defaultdict(list)
    sections = input.split("\n")
    curr_tree = {}
    root = None
    for item in sections:
        num_tabs = item.count("\t")
        name = item.split("\t")[-1]
        if "." not in name:
            curr_tree[num_tabs] = name
        if num_tabs:
            adj[curr_tree[num_tabs - 1]].append(name)
        else:
            root = name
    print('adj', adj)
    longest = 0

    def dfs(node, path):
        nonlocal longest
        for child in adj[node]:
            if "." in name:
                longest = max(longest, sum(map(len, path)) + len(path) + len(child))
            else:
                dfs(child, path + [child])

    dfs(root, [root])
    return longest

res = lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
print('res', res)