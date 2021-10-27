class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        for d in digits:
            new_ones = []
            arr = mapping[d]
            for item in res:
                for letter in arr:
                    new_ones.append(item + letter)
            res = new_ones if len(new_ones) else arr
        return res
            