def second_largest(value):
    big = 0
    unique = set(value)
    for value in unique:
        if value > big:
            big = value
    unique.remove(big)
    return max(unique)

val = [10,5,8,20,15]
print(second_largest(val))