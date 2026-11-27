def stat(nums):
    Largest = float('-inf')
    smallest = float('+inf')
    sum = 0
    average = 0

    for n in nums:
        if n > Largest:
            Largest = n
        elif n < smallest:
            smallest = n
        sum += n
        average = sum / len(nums)
    return (smallest,Largest,round(average,2))

print(stat([4, 9, 2, 7]))
