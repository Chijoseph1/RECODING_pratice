def calculator(a,b):
    operator = input("operator:")
    # print(operator)
    result = []
    v = ""
    if b <= 0 and operator == "/":
        result = "Cannot be divide by zero"
        v = f"Input:{a} | operator: {operator} | input: {b} -> output: {result}"
    if operator == "/":
        result = a/b
        v= f"Input:{a} | operator: {operator} | input: {b} -> result : {result}"
    elif operator == "*":
        result = a*b
        v= f"Input:{a} | operator: {operator} | input: {b} -> result : {result}"
    elif operator == "-":
        result= a-b
        v= f"Input:{a} | operator: {operator} | input: {b} -> result : {result}"
    elif operator == "+":
        result = a+b
        v= f"Input:{a} | operator: {operator} | input: {b} -> result : {result}"
    else:
        result  = "invalid output"
        v= f"Input:{a} | operator: {operator} | input: {b} -> result : {result}"
    return v
    

print(calculator("a",5))