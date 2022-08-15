def main(t, ta):
    o = list(range(2))
    l = 0
    j = 1
    for i in range(len(t)):
        for j in range(len(t)):
            c = int(t[i])+int(t[j])
            if c == ta:
                o[l]=i
                o[l+1]=j
    print(o)


n = str(input())
t = list(n.split(" "))
ta = int(input())
main(t, ta)
