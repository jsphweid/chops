class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # split on dashes
        splitted = s.split("-")
        # merge everything together and uppercase
        joined = "".join(splitted).upper()
        # reverse string
        reversed_str = joined[::-1]
        # divide into groups of k
        i = 0
        groups = []
        while True:
            section = reversed_str[i:i+k]
            if not len(section):
                break
            groups.append(section)
            i += k
        # reverse each group individually
        groups = [s[::-1] for s in groups]
        # reverse whole array
        groups.reverse()
        # join with a dash
        return "-".join(groups)