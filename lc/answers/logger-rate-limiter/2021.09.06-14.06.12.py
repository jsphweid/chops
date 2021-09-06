"""
should be easy with a map that stores the message along with the time of the message
"""

class Logger:

    def __init__(self):
        self._data = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._data or timestamp - self._data[message] >= 10:
            self._data[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)