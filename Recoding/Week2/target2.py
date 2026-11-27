def target_nums(nums,target):
    result = ""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            print(nums[j])
            if nums[i]+ nums[j]== target:
                result=i,j
    print(result)

            # print(nums[j])
        # print(nums[i])


targe = 9
nums =[2,7,11,15]
target_nums(nums,targe)