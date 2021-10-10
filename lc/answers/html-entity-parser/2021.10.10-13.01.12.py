import re
class Solution:
    def entityParser(self, text: str) -> str:
        text = re.sub(r"&quot;", '"', text)
        text = re.sub(r"&apos;", "'", text)
        text = re.sub(r"&gt;", ">", text)
        text = re.sub(r"&lt;", "<", text)
        text = re.sub(r"&frasl;", "/", text)
        text = re.sub(r"&amp;", "&", text)
        return text