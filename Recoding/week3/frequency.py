def frequency(word):
    result ={}
    newword = ""
    punctuation = "?,!@"
    for w in word:
        if w not in punctuation:
            newword += w
    for n in newword.lower().split():
        if n in result:
            result[n] += 1
        else:
            result[n] = 1
        key = None
        largestvalue = -1
    for index,value in result.items():
        if value > largestvalue:
            largestvalue = value
            key = index
            print(f"{key} {largestvalue}")

        # print(f"{index}, {value}")
frequency("python is cool python")
            