class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort_fn(s: str):
            identifier, *contents = s.split(" ")
            is_digit = contents[0].isdigit()
            secondary_sort = "" if is_digit else " ".join(contents)
            tertiary_sort = "" if is_digit else identifier
            return (is_digit, secondary_sort, tertiary_sort)
        return sorted(logs, key=sort_fn)