c = int(input())
r = int(input())
l = []
for i in range(c):
    a = list(map(str, input().split()))
    l.append(a)
print("")
for i in l:
    print(i[0][::-1])
print("")
l.reverse()
for i in l:
    print(*i)