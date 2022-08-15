def main(l,n,s):
    a = []
    for i in range(n):
        c = 0
        for j in range(i,n):
            c += l[j]
            o = []
            if c==s:
                o.append(i+1)
                o.append(j+1)
                a.append(o)
                break
    if len(a)==0: print(-1)
    else: print(a[0][0], a[0][1])

n = int(input())
s = int(input())
l = []
for i in range(n):
    l.append(int(input()))
main(l,n,s)