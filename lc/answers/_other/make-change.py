"""
Count the number of ways to make change for a dollar

$0.50
$0.25
$0.10
$0.05
$0.01


50/50 is 1 method
50/25/25 is another
50/25/10/5/5/5 is another

count_ways(0) -> 0
count_ways(1) -> 1 (1 penny) 
count_ways(2) -> 1 (2 pennies)
count_ways(3) -> 1 (3 pennies)
count_ways(4) -> 1 (4 pennies)
count_ways(5) -> 2 (5 pennies / 1 nickel)
count_ways(6) -> 2 (6 pennies / 1 nickel and 5 pennies)
...
count_ways(10) -> 4 (10p / 1n 5p / 1d / 2n)
count_ways(11) -> 4 (11p / 1n 6p / 1d 1p / 2n 1p)

count_ways(3)
	count_ways(2)
		count_ways(1) -> 1

count_ways(5) 1 +
	count_ways(0) -> 0
	count_ways(4)
		count_ways(3)
			count_ways(2)
				count_ways(1) -> 1

count_ways(11)
	count_ways(10)
		count_ways(9)
			count_ways(8)
				count_ways(7)
					count_ways(6)
						count_ways(5)
							count_ways(4) -> 1 (eventually)
							count_ways(0) -> 0
						count_ways(1) -> 1
					count_ways(2) -> 1 (eventually)
				count_ways(3) -> 1 (eventually)
			count_ways(4) -> 1 (eventually)
		count_ways(5)
			count_ways(4) -> 1 (eventually)
			count_ways(0) -> 0
		count_ways(0) -> 0
	count_ways(6)
		count_ways(5)
			count_ways(4) -> 1 (eventually)
			count_ways(0) -> 0
		count_ways(1) -> 1
	count_ways(1) -> 1
"""

# amount is 100 times the dollar amount (expressed as an integer)
# def count_ways(amount: int) -> int:
# 	if amount == 0: return 0
# 	# if amount == 1: return 1

# 	count = 0
# 	if amount >= 10:
# 		count += count_ways(amount - 10)
# 	if amount >= 5:
# 		count += count_ways(amount - 5)
# 	count += count_ways(amount - 1)

# 	return count

# print(count_ways(11))


# ridiculous every combination
def get_ways(amount: int) -> int:
	ways = []
	def dfs(leftover: int, curr=[]):
		if not leftover: 
			ways.append(curr)
			return
		if leftover >= 50: dfs(leftover - 50, curr + [50])
		if leftover >= 25: dfs(leftover - 25, curr + [25])
		if leftover >= 10: dfs(leftover - 10, curr + [10])
		if leftover >= 5: dfs(leftover - 5, curr + [5])
		dfs(leftover - 1, curr + [1])
	dfs(amount)
	return ways
"""
print(get_ways(11))
yields a list:
	[10, 1], 
	[5, 5, 1], 
	[5, 1, 5], 
	[5, 1, 1, 1, 1, 1, 1], 
	[1, 10], [1, 5, 5], 
	[1, 5, 1, 1, 1, 1, 1], 
	[1, 1, 5, 1, 1, 1, 1], 
	[1, 1, 1, 5, 1, 1, 1], 
	[1, 1, 1, 1, 5, 1, 1], 
	[1, 1, 1, 1, 1, 5, 1], 
	[1, 1, 1, 1, 1, 1, 5], 
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
"""

def get_ways2(amount: int) -> int:
	ways = []
	def dfs(leftover: int, curr=[], max_coin=50):
		if not leftover: 
			ways.append(curr)
			return
		if leftover >= 50 and max_coin >= 50: 
			dfs(leftover - 50, curr + [50], max_coin=50)
		if leftover >= 25 and max_coin >= 25: 
			dfs(leftover - 25, curr + [25], max_coin=25)
		if leftover >= 10 and max_coin >= 10: 
			dfs(leftover - 10, curr + [10], max_coin=10)
		if leftover >= 5 and max_coin >= 5: 
			dfs(leftover - 5, curr + [5], max_coin=5)
		if max_coin >= 1:
			dfs(leftover - 1, curr + [1], max_coin=1)
	dfs(amount)
	return ways

"""
print(get_ways2(11))
	[10, 1], 
	[5, 5, 1], 
	[5, 1, 1, 1, 1, 1, 1], 
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

"""

def count_ways(amount: int, max_coin=50) -> int:
	if amount == 0: return 1

	count = 0
	if amount >= 50 and max_coin >= 50: 
		count += count_ways(amount - 50, max_coin=50)
	if amount >= 25 and max_coin >= 25: 
		count += count_ways(amount - 25, max_coin=25)
	if amount >= 10 and max_coin >= 10: 
		count += count_ways(amount - 10, max_coin=10)
	if amount >= 5 and max_coin >= 5: 
		count += count_ways(amount - 5, max_coin=5)
	if amount >= 1:
		count += count_ways(amount - 1, max_coin=1)
	return count

"""
print('count_ways', count_ways(11)) -> 4
print('count_ways', count_ways(15)) -> 4 but that's wrong
15 => 
	10 + 5
	10 + 1 + 1 + 1 + 1 + 1
	5 + 5 + 5
	5 + 5 + 1 + 1 + 1 + 1 + 1
	5 + 1 + 1 + 1 etc.
	1 + 1 + 1 + 1 etc.
returns 4
"""

#-------------------------------------------------------- GOING TO BED... spent 1 hr

print('count_ways', count_ways(100))  # prints 292

# My main issue was having my exit conditions be
	# if amount == 0: return 0
	# if amount == 1: return 1

# But the correct exit condition is actually 
	# if amount == 0: return 1

# This makes intuitive sense as we know we only want to count when
# we get to 0

#-------------------------------------------------------- WEEKS LATER...

# just refactoring to make it more maintainable

def count_ways_final(amount: int, max_coin=50) -> int:
	if amount == 0: return 1

	count = 0
	for coin in [50, 25, 10, 5, 1]:
		if amount >= coin and max_coin >= coin:
			count += count_ways(amount - coin, max_coin=coin)
	return count

print('count_ways_final', count_ways(100))  # prints 292

# ok how about a dumb one-liner

def fn(a: int, l=50) -> int:
	return 1 if a == 0 else sum(fn(a - c, c) for c in [50, 25, 10, 5, 1] if a >= c and l >= c)

print('one liner', fn(100))  # prints 292
