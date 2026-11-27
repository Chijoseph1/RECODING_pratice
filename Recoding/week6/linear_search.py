def linear(nums,target):
    position = []

    tart = 0
    count = 0
    first = 0
    last = 0
    
    result = ""
    # can they input a list
    #  all this postion stuff 
    for index,num in enumerate(nums) :
        tart = target
        # result = ""
        if num == target:
            position.append(index)
            count += 1
    if count > 0:
        first = position[0]
        last = position[-1]
        result = f"Target: {tart} ---> Found at indices: {position} | Count: {count} | First : {first} | Last : {last}"
    else:
        result =f"Target : {tart} --- > target not found"
    return result 


value =[14,7, 22, 9, 7, 31, 7, 5]
tar = 7
print(linear(value,tar))