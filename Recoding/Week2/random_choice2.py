#1.import random
import random
import test
# 2.Create a list if wordsimport random 
list_of_word = test.word
print(list_of_word)
# pick one word randomly 
word = random.choice(list_of_word)
# initializes attempt to be 5
attempt = 5
# create a list (rexult) containing ynderscore dependent on the length
# result = ["_"] * len(word)
result = ["*"]* len(word)
print(result)
# while loop that tracks if you havent  exhausted your attempt
while attempt > 0 and ("*"in result):
# guess = input a letter
    guess = input("Guest a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                result[i] = guess
    else:
        attempt -=1
        print(f"Wrong guess! you have {attempt} attempts left")
    print(result)
if "*" not in result:
    print(f"The word is {word}, You win")
else:
    print(f"the word is {word}, you lose!")