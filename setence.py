def main(c,t):
    l = []
    for i in range(t):
        o = c[i].split()
        l.append(len(o))
    print(max(l))

t = int(input())
c = []
for i in range(t):
    c.append(str(input()))
main(c,t)