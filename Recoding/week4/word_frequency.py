def wordfrequency(words):
    punctuation = "?!,"
    new_word = " "
    result = {}
    new_value  = 0
    new_key = ""
    # how this work and why is it just joining everything together 
    for word in words:
        if word not in punctuation:
            new_word += word

    for val in new_word.lower().split():
        # print(val)
        # forgotten how to skip punctuation 
        #  how does this work 
        if val in result:
            result[val]+= 1
        else:
            result[val] = 1
    for key,value in result.items():
        if value > new_value:
            new_value = value
            new_key = key
    final_result= f"Most frequent word: {new_key} ({new_value})"
    print(new_key,new_value)
    return final_result
    # print(result)

words="python is fun, and python is powerful!"
print(wordfrequency(words))