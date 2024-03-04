def is_valid(s: str) -> bool:
    stack = []
    for c in s:
        if c in ["(", "[", "{"]:
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ")" and stack[-1] != "(":
                return False
            if c == "]" and stack[-1] != "[":
                return False
            if c == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack

s = input()
if is_valid(s):
    print("yes")
else:
    print("no")