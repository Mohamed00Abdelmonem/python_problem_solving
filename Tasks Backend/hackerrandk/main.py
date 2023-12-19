

x = int(input("enter :"))
y = int(input("enter :"))
z = int(input("enter :"))
n = int(input("enter :"))
result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(result)

#
# empty = []
# list_x = []
# list_y = []
# list_z = []
# if 0 <= x and 0 <= y and 0 <= z and 0 <= n:
#     for i in range(x):
#         list_x.append(i)
#     print(list_x)
#     print(empty.append(list_x))
#
#     for j in range(y):
#         list_y.append(j)
#     print(list_y)
#     print(empty.append(list_y))
#
#     for k in range(z):
#         list_z.append(k)
#     print(list_z)






