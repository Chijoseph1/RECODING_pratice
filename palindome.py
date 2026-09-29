def palidrome(word):
    left = 0
    right = len(word)-1

    while left < right:
        if not word[left].isalnum():
            left+= 1
        if not word[right].isalnum():
            right-=1
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1 
    return True

#  i dont know how to call the function and do soemthing like calling and using
if palidrome("abna"):
    print("A palidrome")
else:
    print("NOt a palidrome")

# print(palidrome("leve ,,l"))

