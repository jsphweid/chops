class StringIterator:
    def __init__(self, compressedString: str):
        digits_buffer = ""
        self.counts = []
        self.chars = []
        for item in compressedString:
            if item.isdigit():
                digits_buffer += item
            else:
                self.chars.append(item)
                if digits_buffer:
                    self.counts.append(int(digits_buffer))
                    digits_buffer = ""
        # there should always be a last digits_buffer
        self.counts.append(int(digits_buffer))

    def next(self) -> str:
        if not self.hasNext():
            return " "
        char = self.chars[0]
        self.counts[0] -= 1

        if self.counts[0] == 0:
            self.counts.pop(0)
            self.chars.pop(0)
        return char

    def hasNext(self) -> bool:
        return len(self.chars) > 0

