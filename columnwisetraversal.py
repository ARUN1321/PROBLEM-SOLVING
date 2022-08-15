c = int(input())
r = int(input())
l = []
for i in range(c):
    a = list(map(int, input().split()))
    l.append(a)
print("")
c = 0
for i in range(len(l)):
    for i in l:
        print(*str(i[c]),end=" ")
    c = c+1

