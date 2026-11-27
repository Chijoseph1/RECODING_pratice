import random

names =["david"]
person = random.choice(names)

attempt= 3
result = []
while attempt > 0:
    guess = input("put a letter: ")
    for value,index in enumerate(person):
        
    attempt -= 1
    