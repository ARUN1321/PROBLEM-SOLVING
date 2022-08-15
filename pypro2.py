import os, json, lz4.block, time

o = str(input())
a = open("enter browser location","rb")
b = a.read(9)
datas = json.loads(lz4.block.decompress(a.read()).decode("utf-8"))
a.close()
present_window = ""

for i in datas.get("windows"):
    for j in i.get("tabs"):
        c = int(j.get("index"))-1
        present_window = j.get("entries")[c].get("url")

print(present_window)

if o in str(present_window):
    print("YES")
    os.system("shutdown")