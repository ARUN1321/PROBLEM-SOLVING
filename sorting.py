def main(l):
    for i in range(len(l)-1):
        if l[i+1]<l[i]:
            l[i+1],l[i] = l[i],l[i+1]
        l = l
    print(l)


n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
main(l)