def target(nums,target):
    dic ={}
    for index in range(len(nums)):
        if target - nums[index] in dic:
            print(dic[target-nums[index]],index)
            break
        dic[nums[index]] = index
    else:
        print("no sum found")

nums = [1,2,3,4]
tar = 4
target(nums,tar)