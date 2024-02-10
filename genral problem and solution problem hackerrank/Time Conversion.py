
# def convert(string):

#       if string[-2:] == "AM" and string[:2] == "12":
#          return "00" + string[2:-2]

#       elif string[-2:] == "AM":
#          return string[:-2]

#       elif string[-2:] == "PM" and string[:2] == "12":
#          return string[:-2]
        
#       else:
#           return str(int(string[:2]) + 12) + string[2:8]

# #driver code
# time="01:58:42PM"
# print("12-hour Format time:: ", time)
# print("24-hour Format time ::",convert(time))






# def findMedian(arr):
#     # Write your code here
#     counter = 0
#     empty_list = []
#     for i in range(arr):
#         counter +=1
#         empty_list.append(counter)
#         midd_num = arr/2
#         empty_list = empty_list[midd_num]
#         print(empty_list)
        
# findMedian(7)        