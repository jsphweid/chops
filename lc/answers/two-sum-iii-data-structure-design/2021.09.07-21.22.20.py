class TwoSum:

    def __init__(self):
        self._sums = set()
        self._nums = []
        

    def add(self, number: int) -> None:
        for num in self._nums:
            self._sums.add(num + number)
        self._nums.append(number)


    def find(self, value: int) -> bool:
        return value in self._sums
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)