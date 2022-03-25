"""
Assuming you can only score:
    2 points - touchback
    3 points - field goal
    7 points - touchdown + 1 point conversion

List all the UNIQUE ways you can score n points.
"""

def helper(target, scores, total, path, res):
    if total == target:
        res.append(path)
    elif total < target:
        for i in range(len(scores)):
            helper(target, scores[i:], total + scores[i], path + [scores[i]], res)


def list_all_ways(target: int):
    scores = [2, 3, 7]
    res = []
    helper(target, scores, 0, [], res)
    return res

print("list_all_ways", list_all_ways(12))