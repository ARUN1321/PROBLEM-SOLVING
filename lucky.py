def main(input1, input2):
    o = input1.split('-')
    o = sum(list(map(int, o)))
    l = sum(list(map(int, str(o).strip())))
    p = sum(list(map(int, str(input2).strip())))
    p = sum(list(map(int, str(p).strip())))
    if l==p: return "Lucky"
    return "Dare"


input1 = str(input())
input2 = int(input())
print(main(input1,input2))
