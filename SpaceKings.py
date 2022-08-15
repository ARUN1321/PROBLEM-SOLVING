def Main(p,q,t):
    c = 0
    ans = 0
    while(len(t)!=0):
        if c%2==0:
            t[-1][0] = t[-1][0]-int(p)
            c = c+1
            if t[-1][0]<=0:
                ans = ans + t[-1][1]
                t.remove(t[-1])
        else:
            t[0][0] = t[0][0]-int(q)
            c = c + 1
            if t[0][0]<=0:
                t.remove(t[0])
    print(ans)         


p,q,n = input().split()
t = []
for i in range(int(n)):
    o = []
    a,b = input().split()
    o.append(int(a))
    o.append(int(b))
    t.append(o)
Main(p,q,t)
