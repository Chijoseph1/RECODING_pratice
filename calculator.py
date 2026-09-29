def calculator():
    # first = input("Input value: ")
    # second = input("Input value: ")
    # i dont know how to safe it and allow the user input number repeatedly like if the user add 5 the *6 it should mutliply by 6 and give result as 30 then i can input -6 and it will still  substract 6 from the equation and give 26 as result i can keep on adding to it and it keep giving me result then if i input undo it give the previous input to me as result 
    while True:
        operator = input("Enter operator: ")
        if operator == "exit":
            break
        part = operator.split()
        number = int(part[1])
        operate = part[0]
        if operate == "*":
            
calculator()