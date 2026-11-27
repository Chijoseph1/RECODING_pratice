def max_subarray_fast(nums):
    if not nums:
        return (0, -1, -1)
    
    max_sum = nums[0]
    running_sum = nums[0]
    
    best_start = 0
    best_end = 0
    current_start = 0 

    for i in range(1, len(nums)):
        if running_sum + nums[i] < nums[i]:
            running_sum = nums[i]
            current_start = i 
        else:
            running_sum += nums[i] 
            
        if running_sum > max_sum:
            max_sum = running_sum
            best_start = current_start
            best_end = i
            
    return (max_sum, best_start, best_end)
