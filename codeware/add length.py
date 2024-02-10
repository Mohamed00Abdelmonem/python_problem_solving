

def add_length(str_):

    result = []
    for word in str_.split():
        result.append(word + " " + str(len(word)))
    return result


    #  or this solution for using by list comprihantion
    # result = [[word , len(word)] for word in str_.split()]

print(add_length("apple ban"))
