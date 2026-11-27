# def fizzbuzz_plus(n):
#     if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
#         return "FizzBuzzBazz"
#     if n % 3 == 0 and n % 5== 0:
#         return "FizzBuzz"
#     if n % 3== 0 and n % 7 == 0:
#         return "FizzBazz"
#     if n % 5 == 0 and n % 7 ==0:
#         return "BuzzBazz"
#     if n % 7 == 0:
#         return "Bazz"
#     if n % 5== 0:
#         return "Buzz"
#     if n % 3 == 0:
#         return "Fizz"
#     return str(n)

def fizzbuzz_plus(nums):
    result = []
    if not nums:
        return result
    for n in range(1,nums+1):
        match (n%3,n%5,n%7):
            case (0,0,0):
                result.append("FizzBuzzBazz")
            case(0,0,_):
                result.append("FizzBuzz")
            case(0,_,0):
                result.append("FizzBazz")
            case(_,0,0):
                result.append("BuzzBazz")
            case(_,_,0):
                result.append("Bazz")
            case(_,0,_):
                result.append("Buzz")
            case(0,_,_):
                result.append("Fizz")
            case _:
                result.append(str(n))
    return result
            
            
print(fizzbuzz_plus(0))
print(fizzbuzz_plus(105))
# print(fizzbuzz_plus(21))
# print(fizzbuzz_plus(35))
# print(fizzbuzz_plus(105))
# print(fizzbuzz_plus(4))