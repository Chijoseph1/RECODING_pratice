import random

random_number = random.randint(1,10)
attempt = 3
while attempt > 0:
    b= int(input("input number: "))
    if b == random_number:
        print("correct")
        break
    elif b != random_number:
        print("try again")
    attempt -= 1
    if attempt == 1:
        print("Your attempt remain one")
    elif attempt == 0:
        print(f"The correct number is: {random_number}")

