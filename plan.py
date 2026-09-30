def nem(nums):
    if nums < 0:
        nums *= nums 
    return nums
print(nem(-6))