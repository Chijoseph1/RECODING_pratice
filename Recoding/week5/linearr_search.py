def linear_search(numbers,target):
    # dic = dict(numbers)
    # how to get the index using dic 
    for index,value in enumerate(numbers) :
        # print(value)
        # how all the when return is inside for loop work and other 
        if value == target:
            return f"Found at index {index}"
    return f"Not found"

num = [14,7,22,9,7,31]
tar = 22
print(linear_search(num,tar))
