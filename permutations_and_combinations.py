from itertools import permutations, combinations

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)

# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')

for p in permutations(items, 2):
    print(p)

# ('a', 'b')
# ('a', 'c')
# ('b', 'a')
# ('b', 'c')
# ('c', 'a')
# ('c', 'b')

for c in combinations(items, 2):
    print(c)

# ('a', 'b')
# ('a', 'c')
# ('b', 'c')

# for combinations() order is not considered
