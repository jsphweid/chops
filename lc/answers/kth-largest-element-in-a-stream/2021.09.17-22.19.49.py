class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._nums = sorted(nums)[-1 * k:]
        self._k = k

    def add(self, val: int) -> int:
        if len(self._nums) == self._k and val <= self._nums[0]:
            return self._nums[0]
        self._nums.append(val)
        self._nums = sorted(self._nums)[-1 * self._k:]
        return self._nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

