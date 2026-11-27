def anagram():
    first = input("First word: ")
    second = input("second word: ")
    anagram = True
    second_list = list(second)
    for i in first:
        if i in second_list:
            second_list.remove(i)
        else:
            anagram = False
            break
    if anagram:
        print("anagram")
    else:
        print("not anagram")
anagram()