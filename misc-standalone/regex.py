"""
given a string and a pattern, return true if it matches

pattern could be `.` or `+` or any [a-z]

def matches(string, pattern) -> bool:
	pass

"""

def matches(string, pattern, previous=None) -> bool:
	if not string and not pattern: return True
	if string and not pattern: return False
	if not string and pattern: return False

	if string[0] == pattern[0] or pattern[0] == ".":
		return matches(string[1:], pattern[1:], string[0])
	elif pattern[0] == "+" and previous == string[0]:
		return matches(string[1:], pattern, previous) or matches(string[1:], pattern[1:], previous)

	return False


def run_asserts(fn):
	assert fn("cat", "cat")
	assert fn("caat", "c..t")
	assert fn("caat", "c.+t")
	assert fn("caaaat", "c.+t")
	assert fn("caaaat", "ca+t")
	assert not fn("cat", "dog")
	assert not fn("cat", "c+")
	assert not fn("cat", "ca+")


print("Running asserts for recursive version...")
run_asserts(matches)

def matches2(string, pattern) -> bool:
	i, j = 0, 0
	while i < len(string) and j < len(pattern):
		if string[i] == pattern[j] or pattern[j] == ".":
			i += 1
			j += 1
		elif pattern[j] == "+":
			if i == 0: return False
			if string[i] == string[i - 1]:
				i += 1
			else:
				j += 1
		else:
			return False
	return i == len(string) and j == len(pattern):

print("Running asserts for iterative version")
run_asserts(matches2)