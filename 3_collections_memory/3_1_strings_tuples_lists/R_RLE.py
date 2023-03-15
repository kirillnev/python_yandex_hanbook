s = input()
ch_last = s[0]
count = 1
for i in range(1, len(s)):
    if s[i] == ch_last:
        count += 1
    else:
        print(ch_last, count, sep=' ')
        count = 1
        ch_last = s[i]
print(ch_last, count, sep=' ')
