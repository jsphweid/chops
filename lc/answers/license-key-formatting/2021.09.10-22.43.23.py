"""
The first method I used involve reversing and re-reversing which just seems over complicated.
If we just knew the length of the first group (which is possibly shortened), that'd probably
make it easier to go in order.

After thinking mathematically for a bit, it's pretty obvious that the remaining chars is the
remainder of the length of the string mod k
i.e. str length 11 mod 4 (k) is 3, which means the 3-4-4
"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        whole = "".join(s.upper().split("-"))
        segments = []
        segment_length = (len(whole) % k) or k
        i = 0
        while True:
            segment = whole[i:i+segment_length]
            if not segment:
                break
            segments.append(segment)
            i += segment_length
            segment_length = k
        return "-".join(segments)
