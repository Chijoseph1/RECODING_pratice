def calculator(a,b):
   nav = input("operator?")
#    print(nav)
   if nav == "/" and b == 0:
      return "cannot divide by zero"
   
   if nav == "-":
      return a - b
   elif nav == "+":
      return a + b
   elif nav == "*":
      return a * b
   elif nav == "/":
      return a / b
   else:
      return "invalid operator"

give =calculator(10,2)
print(give)

a = """nnnannnnn,
nnnnnnll,
nvbzn
"""
print(a)
n = "boy n"
print(n[-8:34])