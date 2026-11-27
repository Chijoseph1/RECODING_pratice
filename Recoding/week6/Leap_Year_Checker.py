def leap_year():
    nums = int(input("input number: "))
    if (nums % 4 == 0 and nums % 100 != 0) or (nums%400 == 0):
        print(f"Input: {nums} ---> {nums} is a leap year")
    else:
        print(f"Input: {nums} ---> {nums} is not a leap year")
leap_year()

