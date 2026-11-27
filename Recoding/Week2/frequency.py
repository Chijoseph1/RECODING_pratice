def frequency(words):
    result ={}
    words.split()
    for word in words.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
        print(result)
    for item,value in result.items():
        print(f"{item}: {value}")


def palin(value):
    result =''
    for i in range(len(value)-1,-1,-1):
        if value== value[i]:
            result ="True"
        else:
            result= "false"
    return result

frequency("python is fun python")
print(palin("boy"))