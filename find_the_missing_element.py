def main(l,n):
    a = sum(l)
    b = n*(n+1)//2
    print(b-a)

n = int(input())
l = []
for i in range(n-1):
    l.append(int(input()))
main(l,n)