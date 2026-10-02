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


result = 0.0
prev_result = []

while True:
    value = input("Input: ").strip()

    if value == "undo":
            if prev_result:
                result =prev_result.pop()
                print(f"result: {result}")
            else:
                 result = 0
                 print("result: {result}")
            continue

    if value == "exit":
         break
     
    operator, operand = value.split()
    calculate = calculator(result, operator,float(operand))
    if isinstance(calculate,str): 
        print(f"result: {calculate}") 
    else:
        prev_result.append(result)
        result = calculate
        print(f"result: {result}")

