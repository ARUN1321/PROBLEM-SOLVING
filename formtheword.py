o = str(input())
o = o.split(':')
b = "abcdefghijklmnopqrstewxyz0"
c = []
for i in o:
    o = []
    for j in i:
        o.append(j)
    c.append(o)
a = ""
for i in c:
    if len(i) == len(set(i)):
        a += b[((b.index(i[0])-b.index(i[-1])))-1]
    else:
        a += i[1]
print(a.upper())
