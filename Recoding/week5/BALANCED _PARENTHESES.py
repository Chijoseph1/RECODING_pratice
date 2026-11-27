use_input = input("Enter input: ").strip()

counter= 0

for ch in use_input:
    if counter < 0:
        break
    if ch in ["(",")"]:
        if ch == "(":
            counter += 1
        else:
            counter -= 1
print(f"balanced" if counter >= 0 else "not balanced")
