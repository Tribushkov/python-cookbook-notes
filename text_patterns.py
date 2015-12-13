# simple stuff

text = 'yeah, but no, but yeah, but no, but yeah'

# exact match
text == 'yeah'  # false

# match at start or end
text.startswith('yeah')  # true
text.endswith('no')  # false

# search for the location of the first occurrence
text.find('no')  # 10

# regular expressions

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

# \d+ means one or more digits
pattern = re.compile(r'\d+/\d+/\d+')

if pattern.match(text1):
    print('yes')
else:
    print('no')

# search for all occurrences of a pattern
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
pattern.findall(text)  # ['11/27/2012', '3/13/2013']

# capture groups
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
m = pattern.match('11/27/2012')

m.group(0)  # '11/27/2012'
m.group(1)  # '11'
m.group(2)  # '27'
m.group(3)  # '2012'
m.groups()  # ('11', '27', '2012')

month, day, year = m.groups()
