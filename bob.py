def Main(o):
    a = []
    r = []
    for i in o:
        if i[0]==1:
            a.append(i[1])
        


t = int(input())
o = []
for i in range(t):
    l = []
    a,b = input().split()
    l.append(a)
    l.append(b)
    o.append(l)
Main(o)
