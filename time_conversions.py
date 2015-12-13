from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b

c.days  # 2
c.seconds  # 37800

# representing specific dates and times
from datetime import datetime

a = datetime(2012, 9, 23)
print (a + timedelta(days=10))  # 2012-10-03 00:00:00
b = datetime(2012, 12, 21)
d = b - a
d.days  # 89

now = datetime.today()
print (now + timedelta(minutes=10))
