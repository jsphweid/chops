class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
    	res = [None] * len(indices)
    	for i, char in enumerate(s):
    		res[indices[i]] = char
    	return "".join(res)
