def prime_number_checker(N):
    final_result = ""
    first = ""
    result = []
    sum = 0

    if prime(N):
         first = (f"{N} is a Prime")
    else:
         first = (f"{N} is not a prime")
         
    for n in range(2,N+1):
        if prime(n):
            result.append(n)
    for v in result:
        sum += v
    final_result = (f"{first}\nPrimes up to {N}: {result}\nSum of prime: {sum}")
    return final_result

def prime(N):
        if N <= 1 :
            return False   
        i = 2
        while i * i <= N:
            if N % i == 0:
                return False
            i +=  1
        return True

    

(print(prime_number_checker(7)))
