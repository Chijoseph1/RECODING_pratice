def digit_sum(n):
    if n // 10 == 0:
        return n # if n % 10 == 1 it return 1 that the base case it end the function n%10 that means n remainder 1 
    return n % 10  + digit_sum(n//10) # so this the remainder to the floor dividion giving use 123 and it keeps reducting until it 1 and they is something call stack division so we stak everything at the end it is added 
print(digit_sum(1234))

# def reverse(text):
#     if len(text) == 0:
#         return ""
#     return text[-1] + reverse(text[:-1])
# print(reverse("boy"))

# def count_(text,letter):
#     if not text:
#         return 0 
#     if text[0] == letter:
#         return 1 +count_(text[1:],letter)
#     else:
#      return 0 + count_(text[1:],letter)# i dont know how to made the function call it andd give the answer and count 
# print(count_("","a"))

# def power(base,exp):
#     if exp == 0:
#         return 1
#     return base * power(base,exp-1)
# print(power(2,10))


