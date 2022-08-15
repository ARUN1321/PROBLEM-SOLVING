# r = int(input())
# c = int(input())
# l = []
# for i in range(r):
#     for j in range(c):
#         a = str(input())
#     l.append(list(a.split(" ")))
# for i in l:
#     print(*i,end=" ")

# R = int(input())
# C = int(input())
# matrix = []
# for i in range(R):
# 	a =[]
# 	for j in range(C):
# 		a.append(int(input()))
# 	matrix.append(a)

# for i in range(R):
# 	for j in range(C):
# 		print(matrix[i][j], end = " ")
# 	print()


# matrix = []
# r = int(input())
# c = int(input())
# for i in range(c):
#    row = list(map(int, input().split()))
#    matrix.append(row)
# print(matrix)

c = int(input())
r = int(input())
l = []
for i in range(c):
    a = list(map(int, input().split()))
    l.append(a)
print("")
for i in l:
    print(*i,end=" ")
