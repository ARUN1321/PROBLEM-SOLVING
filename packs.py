def main(t):
    for i in range(len(t)):
        if i%2==0:
            t[i]= 0
    for i in t:
        if i==0:
            t.remove(i)
    if len(t)!=1:
        main(t)
    else: print(t[0])

n = int(input())
t = []
for i in range(n):
    t.append(i+1)
main(t)
