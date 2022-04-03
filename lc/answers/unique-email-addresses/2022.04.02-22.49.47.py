class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "").split("+")[0]
            res.add("@".join([local, domain]))
        return len(res)