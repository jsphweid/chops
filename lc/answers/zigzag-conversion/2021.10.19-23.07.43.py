class Solution:
    def convert(self, s: str, numRows: int) -> str:
        buckets = ["" for _ in range(numRows)]

        # generate indices
        seq = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        seq = seq * len(s)  # excessive

        for i, char in enumerate(s):
            buckets[seq[i]] += char

        return "".join(buckets)