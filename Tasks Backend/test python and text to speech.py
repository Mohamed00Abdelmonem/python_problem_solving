    
list_stu = []
a = []       

n = int(input())
if 2 <= n <= 5:
   for _ in range(n):
    name = input()
    score = float(input())
    list_stu.append([[name, score]]) 
list_stu.sort(key=lambda x: x[1])
list_stu.remove(min(list_stu,key=lambda x: x[1]))
minimum = min(list_stu,key=lambda x:x[1])
minimum = minimum[1]
for i in list_stu:
  if i[1] == minimum:
    a.append(i[0])
a.sort
for i in a:
  print(sort(i))

           