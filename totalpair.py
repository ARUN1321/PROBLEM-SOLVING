
def totalPairs(N, A, B) -> int:
    # Write your code here.
    if N==3:
        a1 = []
        b1 = []
        c = 0
        a1.append(A[0]+A[-1])
        b1.append(B[0]+B[-1])
        for i in range(N-1):
            a1.append(A[i]+A[i+1])
            b1.append(B[i]+B[i+1])
        for i in range(N):
            if a1[i]>b1[i]:
                c = c+1
        print(c)

    else:
        a1 = []
        b1 = []
        c = 0
        for i in range(N):
            for j in range(N):
                if A[i]!=A[j]:
                    a1.append(A[i]+A[j])
        for i in range(N):
            for j in range(N):
                if B[i]!=B[j]:
                    b1.append(B[i]+B[j])
        a = list(set(a1))
        b = list(set(b1))
        c = 0
        for i in range(N-1):
            if a[i]>b[i]:
                c = c+1
        print(c)

A = [4,8,2,6,2]
totalPairs(5,A,[4,5,4,1,3])



