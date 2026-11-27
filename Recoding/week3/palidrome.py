def palindrome(word):
    newword= ""
    punctuation = "?!, "
    for char in word:
        if char not in punctuation:
            newword += char
    lword = newword.lower()
    print(lword)
    result = ""
    reversed = ""
    for i in range(len(lword)-1,-1,-1):
        reversed += lword[i]
    if lword == reversed:
        result = "A palindrome"
    else:
        result = "not a palindrome"
    return result

print(palindrome("Was it a car or a cat i saw?"))
