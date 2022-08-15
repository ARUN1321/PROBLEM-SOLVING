def main(t):
    print("--------------")
    t.sort(key=lambda x: x[2])
    for ele in t:
        s = [str(a) for a in ele]
        print(" ".join(s))
    print("-------------")
    t.sort(key=lambda x: x[0])
    for ele in t:
        s = [str(a) for a in ele]
        print(" ".join(s))
    print("-------------")
    t.sort(key=lambda x: x[1])
    for ele in t:
        s = [str(a) for a in ele]
        print(" ".join(s))
    print("-------------")
    t.sort(key=lambda x: x[3])
    for ele in t:
        s = [str(a) for a in ele]
        print(" ".join(s))
    print("-------------")


n = int(input())
t = []
for i in range(n):
    o = []
    f, m, l, a = input().split()
    o.append(f)
    o.append(m)
    o.append(l)
    o.append(a)
    t.append(o)
main(t)

# 10
# Johan K Smith 56
# Sam T Wallace 40
# Kelly P Bradford 23
# Eric G Link 33
# Chris N Macon 34
# johan K smith 56
# Terry Q Link 78
# Chris K Macon 24
# Sam T Wallace 35
# Johan P Smith 40

# Kelly P Bradford 23
# Eric G Link 33
# Terry Q Link 78
# Chris K Macon 24
# Chris N Macon 34
# Johan K Smith 56
# Johan P Smith 40
# Sam T Wallace 35
# Sam T Wallace 40
