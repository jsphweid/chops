"""
===== Initial Thoughts =====
seems like brute force is appropriate here because of small constraints

~~Complexity Analysis
Time - O(n^3)
Space - O(n)

FAILED once because it is subset not subarray!
[5,1,6]
get_subsets([5,1,6], [])
    get_subsets([1,6], [5])
        get_subsets([6], [5,1])
            get_subsets([], [5,1,6])
        get_subsets([], [5,6])
    get_subsets([6], [1])
        get_subsets([], [1,6])
    get_subsets([], [6])

[1,3]
get_subsets([1,3],[])
    get_subsets([3],[1])
        get_subsets([],[1,3])
    get_subsets([],[3])

FAILED again because my counting fn modifies the array!

then success

but this is one way of arriving at a subset
def get_subsets(lst, path):
            nonlocal res
            res += get_sum(path)
            for i in range(len(lst)):
                get_subsets(lst[i+1:], path + [lst[i]])

let's do another way
[1,3]
get_subsets(0,[])
    get_subsets(0,[])

Thinking further, we don't even really need a get_sum method if we simply pass down
the accumulated xor total as path.
"""
class Solution:
    def subsetXORSum(self, nums: List[int], i=0, path=0) -> int:
        if i == len(nums):
            return path
        else:
            return self.subsetXORSum(nums, i+1, path ^ nums[i]) + self.subsetXORSum(nums, i+1, path)
