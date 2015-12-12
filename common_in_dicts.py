a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# find keys in common
a.keys() & b.keys()  # { 'x', 'y' }

# find keys in a that are not in b
a.keys() - b.keys()  # { 'z' }

# find (key, value) pairs in common
a.items() & b.items()  # { ('y', 2) }

# make a new dict wirh certion keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# {'x': 1, 'y':2}
