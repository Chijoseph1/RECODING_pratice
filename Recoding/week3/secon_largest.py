def second_largest(number):
    nums = []
    for item in number:
        if item not in nums:
            nums.append(item)
    largest = 0
    second = 0

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    # nums.remove(largest)
    return second
list =[1,2,2,3,5,7,6]
print(second_largest(list))