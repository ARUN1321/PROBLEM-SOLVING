def main(A,N):
    t = sum(A)
    lsum = 0
    for i,num in enumerate(A):
        t -= num
        if lsum==t:
            return i+1
        lsum += num
    return -1


N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
print(main(A,N))
