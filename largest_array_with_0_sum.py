def main(l,n):
    o = 0
    for i in range(len(l)):
        c = 0
        for j in range(i,len(l)):
            c = c+l[j]
            if c==0:
                o = max(o, j-i+1)
    print(o)

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
main(l,n)
