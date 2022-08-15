def possible(l,d,w,c):
    if c==int(l/2):
        return False
    else:
        c = c*d
        o = w[c]+w[c+1]+w[c+2]
        del w[c:c+2]
        w.insert(c,o)
        return w


t = int(input())
for i in range(t):
    l = int(input())
    d = int(input())
    w = list(map(int, input().split()))
    c = 0
    o = possible(l,d,w,c)
    p = o[:]
    p.sort()
    if d==o: print("possible")
    else:
        if possible(l,d,w,c)==False:
            print("impossible")
        else: possible(l,d,w,c+1)
