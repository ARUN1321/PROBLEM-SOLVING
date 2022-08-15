def main(o):
    l = []
    c = 0
    for i in range(len(o)):
        if i+1!=len(o):
            l.append(o[i]+o[i+1])
        else:
            break
    for i in l:
        c = c+i
    print(c)


n = int(input())
t = input().split()
o = []
for i in t:
    o.append(int(i))
o.sort()
main(o)
