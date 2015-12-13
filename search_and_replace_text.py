# simple literal pattern
text = 'yeah, but no, but yeah, but no, but yeah'

text.replace('yeah', 'yep')  # 'yep, but no, but yep, but no, but yep'

# more complicated patterns
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# case sensitive
text = 'UPPER PYTHON, lower python, Mixed Python'

re.findall('python', text, flags=re.IGNORECASE)
# ['PYTHON', 'python', 'Python']

re.sub('python', 'snake', text, flags=re.IGNORECASE)
# 'UPPER snake, lower snake, Mixed snake'
