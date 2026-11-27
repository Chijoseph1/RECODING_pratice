def cap():
    value = input("Enter word: ")
    No_space = ""
    space = " "
    final_word = ""
    result = ""
    newword= ""

    for n in value.split():
        First_letter = n[0]
        if ord(First_letter) >= 97:
            Asci = ord(First_letter) - 32
            char = chr(Asci)
        
        result = char + n[1:]

        newword += result + " "

    for n in newword:
        if space in n:
            continue
        No_space += n
        
    final_word = (f"Capitalized: {newword} \nNo Spaces: {No_space}")
    print(final_word)

cap()