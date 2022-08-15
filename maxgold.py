def main():
    inputString = input("")
    inputList = inputString.split(" ")
    ashaShot, amarShot, n = int(inputList[0]), int(
        inputList[1]), int(inputList[2])

    hp = []
    gold = []
    for i in range(n):
        hpThis, goldThis = input("").split()
        hp.append(int(hpThis))
        gold.append(int(goldThis))

    def dp(origHp, currAsha):
        if(all([i == 0 for i in origHp])):
            return currAsha
        firstAmarIndex = 0
        for index, i in enumerate(origHp):
            if(i > 0):
                firstAmarIndex = index
                break
        origHp[firstAmarIndex] = max(0, origHp[firstAmarIndex] - amarShot)
        maxAns = 0
        tempHp = origHp[:]
        for index, i in enumerate(origHp):
            if(i == 0):
                continue
            if(i <= ashaShot):
                temp = tempHp[index]
                tempHp[index] = 0
                maxAns = max(maxAns, gold[index] + dp(tempHp[:], currAsha))
                tempHp[index] = temp
            else:
                temp = tempHp[index]
                tempHp[index] -= ashaShot
                maxAns = max(maxAns, dp(tempHp[:], currAsha))
                tempHp[index] = temp

        maxAns = max(maxAns, dp(tempHp[:], currAsha))

        return maxAns

    maxAns = 0
    tempHp = hp[:]
    for index, i in enumerate(hp):
        if(i <= ashaShot):
            temp = tempHp[index]
            tempHp[index] = 0
            maxAns = max(maxAns, dp(tempHp[:], gold[index]))
            tempHp[index] = temp
        else:
            temp = tempHp[index]
            tempHp[index] -= ashaShot
            maxAns = max(maxAns, dp(tempHp[:], 0))
            tempHp[index] = temp
    maxAns = max(maxAns, dp(tempHp[:], 0))
    print(maxAns)


main()
