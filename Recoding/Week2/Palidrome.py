def palindrome():
    value = input("Input:")
    print(value)
    # first = 0
    # # print(first)
    # second = len(value)-1

    # while value[first] < value[second]:
    #     print(first)
    #     if value[first] != value[second]:
    #         return False
    #     first += 1
    #     second -=1
    #     return True
    reverse_word = ""
    for v in range(len(value)-1,-1,-1):
        reverse_word += value[v]
        # print(reverse_word)
        result = ""
        if value == reverse_word:
            result ="True"
        else:
            result ="False"
        return result


print(palindrome())
        