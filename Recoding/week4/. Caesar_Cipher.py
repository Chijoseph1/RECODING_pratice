def caesar():
    v = ord("A")
    print(v)
    result = ""
    text = input("Input text: ")
    shift = int(input("Input how many times to shift: "))
    mode = input("Input mode: ")

    punctuation = "?!.@ 1234567890"

    for index,value in enumerate(text):
        if value in punctuation:
            result+= value
            continue
        start = 65 if value.isupper() else 97
        if mode == "encrypt":
            result += chr((ord(value)-start + shift)%26 + start)
        elif mode == "decrypt":
            result += chr((ord(value)-start - shift)%26+start)
        else :
            print("invalid mode")
    return result

print(caesar())