print("Welcom to TODO list")

result = []
while True:
    choices = input("Menu choices: add, view, remove, quit: ").strip().lower()

    if choices == "add" :
        word_toadd  = input("Add word: ")
        print(f"you have successfully added {word_toadd}.")
        result.append(word_toadd)
    elif choices == "remove":
        if not result:
            print("result is empty")
        else:
            while True:
                remove = (input("index to remove: "))
                try:
                    index = int(remove)
                    if index <=1 and index >=len(result):
                        remove_item = result.pop(index-1)
                        print(f"You have successfully remove {remove_item}")
                        break
                    else:
                        print(f"total len {len(result)}and you asked for {index}")
                        continue  
                except ValueError:
                    print("Input a whole number")
    elif choices == "view":
        if result:
            for index,value in enumerate(result,start=1):
                print(index,value)
        else:    
            print("Nothing in the list")
    elif choices == "quit":
        print("Goodbye!!!")
        break
    else:
        print("thank you")
