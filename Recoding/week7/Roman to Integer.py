def roman(figures):
    result = 0
    # create a list 
    numeral = {
        "I" : 1,
        "V" :5,
        "X":10,
        "C":100,
        "D":500,
        "M":1000
    }

    i = 0
    while i < len(figures)-1:
        if numeral[figures[i]] < numeral[figures[i+1]]:
            result -= numeral[figures[i]]
            i+=1
        else:
            result += numeral[figures[i]]
            i+=1
    else:
        result+= numeral[figures[i]]
    return result
    for index,figure in enumerate(figures):
        current_value = numeral[figure]
        if index < len(figures)-1:
            next_value = numeral[figures[index+1]]
            if current_value < next_value:
                result -= current_value
            else:
                result += current_value
        else:
            result+= current_value
    return result
    
    # while 

print(roman("IIIIIIIIIIIXXXXV"))