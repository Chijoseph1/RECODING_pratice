def calculator(result,operator,operand):
    if operator == "*":
        return result*operand
    elif operator == "+":
        return  result + operand
    if operator == "-":
            return  result-operand
    elif operator == "/":
            if operand == 0:
                 return "cannot be divide by zero"
            return  result / operand
    else:
         return "Invalid operator"


result = 0
prev_result = []
# i dont now to do and store previous result, i dont know how all this work store previous result and get it 

while True:
    value = input("Input: ").strip()
    #  i dont know how to get the if it we click undo like undo  to give the previous result dont know how to get the undo value and work on it 
    if value == "undo":
         prev_result.pop()
         print(prev_result[-1])
         continue
        #  how will i block it from seeing this when it see undo i dont know who to go about that 
    # how i dont u=know who to make it previous number be only int like for example / 0 mean cannt be divide by zero but after it print this he does not have to store it in previous result and when i mutiply or divide again it shpuuld still the previus result remain in result 
    operator, operand = value.split()
    calculate = calculator(result, operator,int(operand))
    if isinstance(calculate,str): 
        print(f"result: {calculate}") 
    else:
        prev_result.append(result)
        result = calculate
        print(f"result: {result}")
        #  result should be what every will append like when i clicjk undo result should be 5 not 10 bn which was trhe formal result how will i go about thaty

