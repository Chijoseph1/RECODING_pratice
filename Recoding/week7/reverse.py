def palindrome(word):
    reverse = ""
    result = ""
    for char in word:
        reverse = char + reverse

        if word != reverse:
            result = False
        else:
            result = True
    return result
value = "racecar"
if palindrome(value):
    print(f"{value} is a palidrome.")
else:
    print(f"{value} is not a palindorme")
# print(palindrome("racecar"))