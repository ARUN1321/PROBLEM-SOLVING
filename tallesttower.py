def main(inputs):
    inputs.sort(key=lambda x: x[0])
    c = []
    for i in inputs:
        if len(c) != 0:
            if int(c[-1][-1]) > int(i[1]):
                inputs.remove(c[-1])
            else:
                c.append(i)
        else:
            c.append(i)
    for ele in inputs:
        s = [str(a) for a in ele]
        print(",".join(s))


inputs = []
while True:
    a = input()
    if a == "":
        break
    d = a.split(',')
    inputs.append(d)
main(inputs)

# 64,120
# 65,100
# 70,150
# 56,90
# 75,190
# 60,95
# 68,110
