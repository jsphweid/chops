import re
class StringIterator:

    def __init__(self, compressedString: str):
        self.nums = [int(n) for n in re.findall(r"\d+", compressedString)]
        self.chars = re.findall(r"[a-zA-Z]", compressedString)
        

    def next(self) -> str:
        if not len(self.nums): return " "
        if self.nums[0] == 1:
            self.nums.pop(0)
            return self.chars.pop(0)
        else:
            self.nums[0] -= 1
            return self.chars[0]
        

    def hasNext(self) -> bool:
        return len(self.nums) != 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()