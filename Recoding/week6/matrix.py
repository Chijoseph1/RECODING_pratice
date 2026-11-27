def matrix(nums):
    result = []
    v = []
    total_result = ""
    append_result = ""
    for num in nums:

        total = 0
        for i in num:
            total += i
            average = total / len(num)
            result.append(total)
            v.append(average)

v = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
matrix(v)