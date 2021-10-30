class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for l in logs:
            if l.split(" ")[1][0].isdigit():
                digit_logs.append(l)
            else:
                letter_logs.append(l)
        def map_log(log):
            identifier, *content = log.split(" ")
            return " ".join(content) + " aaaa" + identifier
        letter_logs.sort(key=map_log)
        return letter_logs + digit_logs


