"""
given a string and a pattern, return true if it matches

pattern could be `.` or `+` or any [a-z]

def matches(string, pattern) -> bool:
	pass

"""

def matches(string, pattern, previous=None) -> bool:
	if not string and not pattern: return True
	if string and not pattern: return False
	if not string and pattern: return False  # hmm...

	if string[0] == pattern[0] or pattern[0] == ".":
		return matches(string[1:], pattern[1:], string[0])
	elif pattern[0] == "+" and previous == string[0]:
		return matches(string[1:], pattern, previous) or matches(string[1:], pattern[1:], previous)

	return False


assert matches("caat", "c..t")
assert matches("caat", "c.+t")
assert matches("caaaat", "c.+t")
assert matches("caaaat", "ca+t")
assert matches("cat", "cat")
assert not matches("cat", "dog")
assert not matches("cat", "c+")
assert not matches("cat", "ca+")