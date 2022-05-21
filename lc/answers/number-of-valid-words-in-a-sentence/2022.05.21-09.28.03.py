def has_digit(candidate):
    for char in candidate:
        if char.isdigit():
            return False
    return True


def has_valid_hyphen(candidate):
    num_hyphens = candidate.count("-")
    if num_hyphens == 0:
        return True
    if num_hyphens > 1:
        return False

    for i, char in enumerate(candidate):
        if char == "-":
            return i != 0 and i != len(candidate) - 1 and candidate[i-1].islower() and candidate[i+1].islower()
    return False


def has_valid_punc(candidate):
    punc = {".", ",", "!"}
    num_punc = len([c for c in candidate if c in punc])
    if num_punc > 1:
        return False
    if num_punc == 0:
        return True
    return candidate[-1] in punc


class Solution:
    def countValidWords(self, sentence: str) -> int:
        candidates = [c for c in sentence.split(" ") if c != ""]
        return sum([has_digit(c) and has_valid_hyphen(c) and has_valid_punc(c) for c in candidates])
