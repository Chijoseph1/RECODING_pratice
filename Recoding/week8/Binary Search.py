def binary(nums,target):
    low = 0
    high = len(nums)-1
    result  = -1
    count = 0 
    # compare = []

    while low <= high :
        # how will i divide it into 2 and take it to the half then check 
        middle = (low + high) // 2
        count+=1
        if nums[middle] > target:
            high = middle -1
        elif nums[middle] < target:
            low = middle +1
        else:
            result  = middle
            high = middle -1
    return f"nums = {nums} target = {target} --> {(result,count)}"

nums =  [1,4,4,4,4,4,4,4,4,4]
target = 4
print(binary(nums,target))


