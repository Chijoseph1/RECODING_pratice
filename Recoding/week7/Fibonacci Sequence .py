def fibo(N):
    reverse = ""
    fibo_l = ""
    count_of_value = ""
    a = 0
    b = 1
    sum_of_value = 0
    while a <= N:
        fibo_l +=  str(a) + ","
        # MUltiple variable stuff :- expecially useful when updating two variable that depend on each other previous values.
        a,b = b,a+b
    for n in fibo_l:
        if n.isdigit():
            if int(n) % 2 == 0:
                count_of_value +=n
                sum_of_value+= int(n)
        reverse = n + reverse
    # for n in count_of_value:

    final_result = (f"Sequence: {fibo_l.rstrip(",")}\nEven sum: {sum_of_value}  (which is {count_of_value})\nReversed: {reverse.lstrip(",")}")
    return final_result
print(fibo(8))
