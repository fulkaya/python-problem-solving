def echo_validator(text: str) -> bool:
    new_text = text.replace(" ", "").lower()

    if not new_text:
        return False

    mid = len(new_text) // 2
    for i in range(mid):
        if new_text[i] != new_text[-1 - i]:
            return False

    return True

if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("hello"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator("  "))
            

