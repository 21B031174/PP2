from datetime import datetime

d = datetime(2022, 1, 1, 1, 1, 1)

now=datetime.now()

tday=now.today().replace(microsecond=0)

a=tday-d

b=a.days*24*3600+a.seconds
print(b)
