# بالطبع، سأشرح المسألة باللهجة المصرية.

# المسألة بتقول إن عندك مصفوفة مربعة، والمطلوب إنك تحسب الفرق المطلق بين مجموع العناصر على القطر الرئيسي (من الزاوية العلوية اليسرى إلى الزاوية السفلية اليمنى) وبين مجموع العناصر على القطر الثانوي (من الزاوية العلوية اليمنى إلى الزاوية السفلية اليسرى).

# مثال:
# إذا كانت المصفوفة زي دي:

# ```
# 1  2  3
# 4  5  6
# 9  8  9
# ```

# القطر الرئيسي هو 1 + 5 + 9 = 15
# القطر الثانوي هو 3 + 5 + 9 = 17

# الفرق المطلق هو |15 - 17| = 2

# الوظيفة اللي لازم تكتبها هنا هي `diagonalDifference` واللي هتاخد المصفوفة وترجعلك الفرق المطلق بين مجموع العناصر على القطر الرئيسي والقطر الثانوي.

# أي استفسار إضافي أنا تحت أمرك.


# def function(line1, line2, line3):
#     x = line1[0]
#     xx = line2[1]
#     xxx = line3[2]
#     result1 = sum((x,xx,xxx))
#     y = line1[2]
#     yy = line2[1]
#     yyy = line3[0]
#     result2 = sum((y,yy,yyy))
#     print(line1)
#     print(line2)
#     print(line3)
#     print (result1)
    
#     return result2
# print(function([2,3,1],[5,4,2], [6,4,2]))
        
        

def calculate_diagonal_difference(line1, line2, line3):
    first_diagonal_elements = [line1[0], line2[1], line3[2]]
    second_diagonal_elements = [line1[2], line2[1], line3[0]]
    
    result1 = sum(first_diagonal_elements)
    result2 = sum(second_diagonal_elements)
    print (f''' 
{line1}
{line2}
{line3}''')
           
    # print(result1)
    # print(result2) 
    print (abs(result1-result2))

calculate_diagonal_difference([11,2,4],[4,5,6], [10,8,-12])
        

