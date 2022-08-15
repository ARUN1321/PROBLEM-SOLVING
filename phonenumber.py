def getPhoneNumber(s):
    number = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7'
    ,'eight':'8','nine':'9','zero':'0'}
    phone = list(s.split(" "))
    res = []
    for i in range(len(phone)):
        if phone[i]=="double":
            res.append(number.get(phone[i+1]))
        if phone[i]=="triple":
            res.append(number.get(phone[i+1]))
        else:
            res.append(number.get(phone[i]))
    print(res)

s = "five eight double two triple two four eight five six"
getPhoneNumber(s)