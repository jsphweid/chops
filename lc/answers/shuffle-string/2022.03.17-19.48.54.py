"""
failed once because I wasn't thinking clearly

failed twice because...?
s = "codeleet", indices = [4,5,6,7,0,2,1,3]

could be because "".join() is not how you join a list of strings?
no, that should work

Actually... I fundamentally misunderstood the problem
"".join([s[i] for i in indices])
is a solution for if the chars at indices go in that order

The 4 tells c to go at position 4
Not the 0th position gets the char at position 4


"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
    	res = [None] * len(indices)
    	for i, char in enumerate(s):
    		res[indices[i]] = char
    	return "".join(res)