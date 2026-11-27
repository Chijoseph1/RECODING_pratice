def two_sum(nums,target):
    dic = {}
    for index,value in enumerate(nums):
        calculate = target - value    
        print(calculate)   
        if calculate in dic:
            return [calculate,dic[index]]
        dic[value] = index
    else:
        print("no")
        # print(calculate)

nums = [2,3,5,4]
target = 6
print(two_sum(nums,target))

#  k %= len(nums) if nums else 1
#     return nums[-k:] + nums[:k]
# explain very well why we need the if 