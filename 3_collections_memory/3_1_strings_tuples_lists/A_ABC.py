start_letter = ('а', 'б', 'в')
n_words = int(input())
words = [input() for i in range(n_words)]
count = 0
for word in words:
    count += 1 if word[0] in start_letter else 0
print('YES' if count == len(words) else 'NO')
