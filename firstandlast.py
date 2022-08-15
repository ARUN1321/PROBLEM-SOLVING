def main(o,n):
    c = []
    if len(c) == 0:
        c.append(o[0]+o[-1])
    for i in range(n-1):
        c.append(o[i]+o[i+1])
    return max(c)


t = int(input())
for i in range(t):
    n = int(input())
    o = list(map(int, input().split()))
    print(main(o,n))
