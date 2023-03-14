n = int(input())
bb = [int(input()) for i in range(n)]
h_l = 0
is_all = True
for i in range(n):
    m = bb[i] // 256**2
    r = bb[i] % 256**2 // 256
    h = 37 * (m + r + h_l) % 256
    b = h + r * 256 + m * 256**2
    h_l = h
    if h >= 100 or b != bb[i]:
        print(i)
        is_all = False
        break

if is_all:
    print(-1)
