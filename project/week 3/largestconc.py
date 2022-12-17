def largestconcatenate (numbers):
    list = [i for i in numbers]
    result=[]
    for x in range(len(list)):
        max_num=max(list)
        result.append(max_num)
        list.remove(max_num)
    return result
print(largestconcatenate("145164"))




