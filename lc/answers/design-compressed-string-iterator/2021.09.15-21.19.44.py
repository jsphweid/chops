"""
obviously we could just uncompress it all in the constructor and server it up using pop(0). let's do 
that as a first pass

Actually it's not acceptable for a first pass...

Here's what I originally had:
```
    def __init__(self, compressedString: str):
        self.uncompressed_string = ""
        char_buffer = ""
        digit_buffer = ""
        for c in compressedString:
            if c.isdigit():
                digit_buffer += c
            else:
                if digit_buffer:
                    self.uncompressed_string += (char_buffer * int(digit_buffer))
                    digit_buffer = ""
                    char_buffer = ""
                char_buffer += c
        if digit_buffer:
            self.uncompressed_string += (char_buffer * int(digit_buffer))
        self.uncompressed_string = list(self.uncompressed_string)
        

    def next(self) -> str:
        return self.uncompressed_string.pop(0) if self.hasNext() else " "

    def hasNext(self) -> bool:
        return len(self.uncompressed_string) > 0
```

second solution passed all tests but took too much memory still apparently

```
    def __init__(self, compressedString: str):
        self.compressed_string = list(compressedString)
        self.temp = []

    def next(self) -> str:
        if len(self.temp):
            return self.temp.pop(0)
        if not len(self.compressed_string):
            return " "
        alpha_buffer = ""
        digit_buffer = ""
        while len(self.compressed_string):
            char = self.compressed_string[0]
            if char.isalpha():
                if digit_buffer:
                    break
                else:
                    alpha_buffer += char
            else:
                digit_buffer += char
            self.compressed_string.pop(0)
        generated = alpha_buffer * int(digit_buffer) # ee or l
        self.temp.extend(list(generated)[1:])
        return generated[0]

    def hasNext(self) -> bool:
        return (len(self.compressed_string) + len(self.temp)) > 0
```

I wonder if we were to store two lists of half size, one for numbers and one for strings

"""

class StringIterator:

    def __init__(self, compressedString: str):
        self.alphas = []
        self.nums = []
        digit_buffer = ""
        for char in compressedString[::-1]:
            if char.isdigit():
                digit_buffer += char
            else:
                self.alphas.insert(0, char)
                self.nums.insert(0, int(digit_buffer[::-1]))
                digit_buffer = ""

    def next(self) -> str:
        if not self.hasNext():
            return " "

        ret = self.alphas[0]
        if self.nums[0] == 1:
            self.nums.pop(0)
            self.alphas.pop(0)
        else:
            self.nums[0] -= 1
        return ret


    def hasNext(self) -> bool:
        return len(self.nums) > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()