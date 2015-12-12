
words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)  # [('eyes', 8), ('the', 5), ('look', 4)]

# some other Counter good stuff

morewords = ['why','are','you','not','looking','in','my','eyes']

a = Counter(words)
b = Counter(morewords)

# combine and subtract counts
c = a + b
d = a - b
