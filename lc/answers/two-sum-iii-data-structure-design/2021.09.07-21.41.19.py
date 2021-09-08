from collections import defaultdict

class TwoSum:

    def __init__(self):
        self._dict = defaultdict(int)
        

    def add(self, number: int) -> None:
        self._dict[number] += 1 
        

    def find(self, value: int) -> bool:
        for num, quantity in self._dict.items():
            compliment = value - num
            if compliment in self._dict:
                if compliment == num:
                    if quantity > 1:
                        return True
                else:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)