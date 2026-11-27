def palindrome(word):
    punctuation = "!?,@"
    new_word = ""
    for val in word:
        if val not in punctuation:
            new_word += val
    final_word =new_word.lower()
    result =""
    right = len(final_word)-1
    left = 0
    # dont knw whether is for loop of if statement 
    while left < right :
        #  my skipping logic , i dont really know how it works
        if final_word[right] != final_word[left]:
            print(final_word[right],final_word[left])
            result = "False"
            left+=1
            right -= 1
        else:
            result = "True"
        return result


word = "Was it a car or a cat I saw?"

print(palindrome(word))
    