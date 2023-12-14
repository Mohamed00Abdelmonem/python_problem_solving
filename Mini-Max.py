# def min_max(*args):
#     arr = list(args)  # Convert the arguments to a list
#     sum_small = sum(arr) - max(arr)  # Sum of all elements except the largest one
#     sum_more = sum(arr) - min(arr)  # Sum of all elements except the largest one
#     print(sum_small, sum_more)

# min_max(3, 5, 6,1, 2)



def min_max_sum(*args):
    convert_to_list = list(args)
    sum_small=sum(convert_to_list)-max(convert_to_list)
    sum_more=sum(convert_to_list)-min(convert_to_list)
    print(sum_small, sum_more)


min_max_sum(3,5,2,1,6)    