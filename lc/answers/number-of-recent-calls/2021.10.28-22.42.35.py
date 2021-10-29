class RecentCounter:

    def __init__(self):
        self._calls = []

    def ping(self, t: int) -> int:
        self._calls.append(t)
        while t - self._calls[0] > 3000:
            self._calls.pop(0)
        return len(self._calls)
