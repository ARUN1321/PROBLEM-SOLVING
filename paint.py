# You are using Python
def main(o):
    for i in range(len(o)-1):
        if o[i+1]!=0:
            o[i]+=o[i+1]
            o[i+1]=0
        else:
            continue
    return o


n = int(input())
o = list(map(int, input().split()))
o = main(o)
o.sort(reverse=True)
print(*o,sep=" ")
