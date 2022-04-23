class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.pages = [homepage]

    def _get_current_page(self):
        return self.pages[self.i]

    def visit(self, url: str) -> None:
        self.i += 1
        self.pages = self.pages[:self.i]
        self.pages.append(url)

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self._get_current_page()

    def forward(self, steps: int) -> str:
        self.i = min(len(self.pages) - 1, self.i + steps)
        return self._get_current_page()


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)