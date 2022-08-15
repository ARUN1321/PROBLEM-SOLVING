n = int(input())
t = []
for i in range(n):
    t.append(i+1)
f = [t[i * 5:(i + 1) * 5] for i in range((len(t) + 5 - 1) // 5 )]
c = 0
l = []
l1 = []
for i in range(len(f)):
    if i%2!=0:
        l.append(f[i])
    else: l1.append(f[i])
l.reverse()
ans = l1+l
for i in ans:
    print(*i, sep=" ")
