n = int(input())
headers = [input() for _ in range(n)]
query = input()

for header in headers:
    if header.lower().find(query.lower()) != -1:
        print(header)