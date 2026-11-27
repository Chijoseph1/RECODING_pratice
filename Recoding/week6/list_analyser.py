def analyser(nums):
    # i dont know how to use this
    Smallest = float("inf")
    Largest = float("-inf")
    Total = 0
    Average = 0
    position = 0 
    position_small = 0
    Numbers_above_average = 0
    # print(position)
# how to make a value keep reseting 
    for index,num in enumerate(nums):
        if num > Largest:
            Largest = num
            position = index
        elif num < Smallest:
            Smallest = num
            position_small = index
            # position = 0
        Total += num
        Average = Total / len(nums)
    print(position)
    for num in nums:
        
        if num > Average:
            Numbers_above_average += 1
    print(f"Smallest: {Smallest} (at index {position_small}_\nLargest: {Largest}(at index {position})\nTotal: {Total}\nAvarage: {Average:.2f}\nNumbers above average: {Numbers_above_average}")

num = [12, 5, 27, 8, 14, 27, 3]
analyser(num)