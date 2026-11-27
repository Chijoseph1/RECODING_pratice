def is_balanced(text):
    stack = []
    bracket = {")":"(","]":"[","}":"{"}
    for char in text:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket:
            if not stack or bracket[char] != stack.pop():
                return False

    return len(stack) == 0

print(is_balanced("(a + b) * [c - d]")) #true
print(is_balanced("{[()]}"))             # True
print(is_balanced("([)]")  )              # False
print(is_balanced("((]")    )              # False
print(is_balanced("}{")    )              # False
print(is_balanced("")      )              # True
