n = int(input())
points = [input().split() for _ in range(n)]
routs = dict()
for i in range(n):
    cur = (points[i][0][:-1], points[i][1][:-1])
    if cur not in routs:
        rout = [cur]
        for j in range(n):
            if (i != j and
                    cur[0] == points[j][0][:-1] and
                    cur[1] == points[j][1][:-1]):
                rout.append((points[j][0][:-1], points[j][1][:-1]))
        routs[cur] = len(rout)
print(max(routs.values()))
