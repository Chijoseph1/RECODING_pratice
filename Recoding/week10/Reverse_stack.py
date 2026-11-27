def reverse(nums):
    if not nums:
        return nums
    return reverse(nums[-1]) + reverse(nums[:-1])
# my logic is not logicing 

stack = [1, 2, 3, 4, 5]
print(reverse(stack))
         
