def bracket_validator(s: str) -> bool:
    justbrackets = ""
    for bracket in s:
        if bracket in "(){}[]":
            justbrackets += bracket
    
    while "()" in justbrackets or "[]" in justbrackets or "{}" in justbrackets:
        justbrackets = justbrackets.replace("()", "")
        justbrackets = justbrackets.replace("[]", "")
        justbrackets = justbrackets.replace("{}", "")

    return justbrackets == ""

if __name__ == "__main__":
    print(bracket_validator("()"))
    print(bracket_validator("()[]{}"))
    print(bracket_validator("(]"))
    print(bracket_validator("([)]"))
    print(bracket_validator("{[]}"))
    print(bracket_validator("hello(world)"))
    print(bracket_validator("((())"))
    print(bracket_validator(""))