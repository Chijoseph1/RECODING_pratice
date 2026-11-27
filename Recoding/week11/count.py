def count_letters(text):
    vowel = "aeiou"
    consonant = "bcdfghjklmnpqrstvwxyz"
    count_vowel = 0
    count_consonant = 0

    for n in text.lower():
        if n in vowel:
            count_vowel += 1
        elif n in consonant:
            count_consonant += 1
    return (count_vowel,count_consonant)
print(count_letters("fffhjydfw"))