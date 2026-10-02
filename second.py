def second(number):
    largest = 0
    second_largest = 0
    for i in number:
        if i > largest:
            largest = i
    print(largest)

num = [9,8,6,5]
second(num)
