class Logger:

    def __init__(self):
        self._mapping = {}        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self._mapping and self._mapping[message] + 10 > timestamp:
            return False
        self._mapping[message] = timestamp
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)