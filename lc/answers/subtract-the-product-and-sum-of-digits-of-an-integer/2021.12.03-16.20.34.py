class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(a) for a in list(str(n))]
        s, p = 0, 1
        for num in nums:
            s += num
            p *= num
        return p - s