def second_largest(num):
    largest = 0
    second_largest = 0
    for n in num :
        if n > largest:
            second_largest=largest
            largest = n
            # print(second_largest)
        elif n < largest and n > second_largest:
            second_largest = n
    return second_largest

print(second_largest([1,2,3,3]))
