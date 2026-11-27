def duplic(nums):
    dict = {}
    result = []
    for n in nums:
        if n in dict:
           dict[n] += 1
        else:
           dict[n] = 1
    # how to do the printing stuff
    for index,value in dict.items():
        if value > 1:
            result.append(index)
        # print(dict)
    return result if result else "No duplicates"

v=[1,3,3] 
print(duplic(v))
