def binary(Num):
    # how to store the remainder of a value
#    n = Num // 2
    result = []
    finally_result = ""
    while Num > 0:
        remainder = Num % 2
        result.append(remainder)
        Num = Num // 2
    for num in result:
        finally_result += str(num)
    print(f"input: {Num} ---> Output: {finally_result}")
binary(10)