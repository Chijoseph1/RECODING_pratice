def subset(nums,target,i=0):
    if not target:
        return True
    if i == len(nums):
        return False
    include = subset(nums,target-nums[i],i+1)
    exclude = subset(nums,target,i+1)
    return include or exclude

nums = [2, 4, 6, 10]
target = 16
print(subset(nums,target))