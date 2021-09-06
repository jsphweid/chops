class MovingAverage:

    def __init__(self, size: int):
        self._size = size
        self._vals = []
        

    def next(self, val: int) -> float:
        self._vals.append(val)
        window = self._vals[-1 * self._size:]
        return sum(window) / len(window)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)