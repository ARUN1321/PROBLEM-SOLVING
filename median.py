def main(o,a):
    b = a+o
    b.sort()
    if len(b)%2:
        return (b[int(len(b)/2)]+b[int((len(b)/2)-1)])/2
    else: return (b[int(len(b)/2)])

o = list(map(int, input().split()))
a = list(map(int, input().split()))
print(main(o,a))