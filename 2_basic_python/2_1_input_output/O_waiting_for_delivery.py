from datetime import timedelta

n = int(input())
m = int(input())
t = int(input())

t1 = timedelta(hours=n, minutes=m)
t2 = timedelta(minutes=t)
t3 = t1 + t2
secs = t3.total_seconds() % (24 * 60 * 60)
hours = int(secs // (60 * 60))
minutes = int(secs % (60 * 60) // 60)
str_time = ''
str_time += '0' if hours < 10 else ''
str_time += str(hours) + ':'
str_time += '0' if minutes < 10 else ''
str_time += str(minutes)

print(str_time)
