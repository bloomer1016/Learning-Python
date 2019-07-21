smallest = None
print('Before:', smallest)
for itervar in [3, 42, 12, 9, 74, 15]:
	if smallest is None or itervar < smallest:
		smallest = itervar
	print('Loop:', itervar, smallest)
print('Smallest:', smallest)