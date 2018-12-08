import random

lst = random.sample(range(1, 1000000), 999999)

for i in range(len(lst)):
	smallest = min(lst[i:])
	smallest_i = lst.index(smallest)
	tmp = lst[i]
	lst[i] = smallest
	lst[smallest_i] = tmp

print lst