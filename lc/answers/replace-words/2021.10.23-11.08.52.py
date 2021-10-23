import re
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        joined = "|".join(dictionary)
        def fix(word):
            return re.sub(rf"^({joined})\w+$", r"\1", word)
        return " ".join([fix(word) for word in sentence.split(" ")])
