s = input()
s_proc = s.lower().replace(' ', '')
print('YES' if s_proc == s_proc[::-1] else 'NO')
