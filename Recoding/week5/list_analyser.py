def analyser(numbers):
    dic = {
        "Smallest":float("inf"),
        "Largest":float("-inf"),
        "Total":0,
        "AVerage":0
    }
    # dic["Smallest"] = numbers[0]
    for i in numbers:
        if i > dic["Largest"]:
            dic["Largest"] = i
        # i dont know how to manipulate it to find the smallest number in the list
        if i < dic["Smallest"]:
            dic["Smallest"] = i
        dic["Total"] += i
        dic["AVerage"] = dic["Total"] / len(numbers)
    return dic

input = [-12,-5,-27,-8,-14]
print(analyser(input))
