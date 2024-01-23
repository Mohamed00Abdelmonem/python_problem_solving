# x='''
# 1 2 3
# 4 5 6
# 9 8 9 
# '''
# arr= [
#     [1,2,3],
#     [4,5,6],
#     [9,8,9],
# ]


def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0 
    o= 1
    for x  in range(len(arr)):    
        sum1 += arr[x][x]
        sum2 += arr[x][-o]
        o += 1
        
    print(abs(sum1 -sum2))
diagonalDifference([[1,2,3],
                    [4,5,6],
                    [9,8,9]])   
                    