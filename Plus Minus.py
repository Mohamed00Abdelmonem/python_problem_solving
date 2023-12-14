# n = int(input().strip())

# arr = list(map(int, input().rstrip().split()))


# print(arr)

# def fun(*args):
#     empty_list= [args]
#     n = []
#     p = []
#     count_n = 0
#     count_p= 0
   
#     for i in str(empty_list):
#         if i > 0 :
#             count_n+= 1
#             result2= n.append(count_n)
            
#         elif i < 0 :
#             count_p+= 1
#             result = n.append(count_p)

#     print(result2,result2)
# fun(2,-4,-2,5,6)


# def fun(*args):
#     n = []  # for negative numbers
#     p = []  # for positive numbers
#     z = []  # for zero number
#     count_n = 0
#     count_p = 0
#     zero = 0


#     for i in args:
#         if i > 0:
#             count_p += 1
#             p.append(count_p)
#             result_p = len(p) / len(args)

#         elif i < 0:
#             count_n += 1
#             n.append(count_n)
#             result_n = len(n) / len(args)

#         elif i == 0:
#             zero += 1
#             z.append(zero)
#             result_z = len(z) / len(args)


#     print(result_p)
#     print(result_n)
#     print(result_z)

# fun(2, -4, -2,0, 5, 6)







# def plusMinus(arr):
#     # Count occurrences of positive, negative, and zero numbers using list comprehensions
#     count_positive = sum(1 for num in arr if num > 0)
#     count_negative = sum(1 for num in arr if num < 0)
#     count_zero = sum(1 for num in arr if num == 0)

#     # Calculate the ratios
#     total_elements = len(arr)
#     ratio_positive = count_positive / total_elements
#     ratio_negative = count_negative / total_elements
#     ratio_zero = count_zero / total_elements

#     # Print the ratios with 6 decimal places
#     print("{:.6f}".format(ratio_positive))
#     print("{:.6f}".format(ratio_negative))
#     print("{:.6f}".format(ratio_zero))







# def plusMinus(arr):
#     # Initialize counters for positive, negative, and zero values
#     count_positive = 0
#     count_negative = 0
#     count_zero = 0

#     # Iterate through each element in the array
#     for number in arr:
#         # Check if the number is positive, negative, or zero
#         if number > 0:
#             count_positive += 1
#         elif number < 0:
#             count_negative += 1
#         else:
#             count_zero += 1

#     # Calculate the ratios
#     ratio_positive = count_positive / len(arr)
#     ratio_negative = count_negative / len(arr)
#     ratio_zero = count_zero / len(arr)

#     # Print the ratios with 6 decimal places
#     print("{:.6f}".format(ratio_positive))
#     print("{:.6f}".format(ratio_negative))
#     print("{:.6f}".format(ratio_zero))
