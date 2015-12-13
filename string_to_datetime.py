from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now
diff = z - y

nice_z = datetime.strftime(z, %A %B %d, %Y)  # 'Sunday September 23, 2012'
