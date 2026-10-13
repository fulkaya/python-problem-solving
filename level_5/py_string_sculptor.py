def string_sculptor(text: str) -> str:
    result = []
    alpha_count = 0

    for char in text:
        if char == " ":
            alpha_count = 0
            result.append(char)
        elif char.isalpha():
            if alpha_count % 2 == 0:
                result.append(char.lower())
            else:
                result.append(char.upper())
            alpha_count += 1
        else:
            result.append(char)

    return "".join(result)


if __name__ == "__main__":
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor("abc123def"))
    print(string_sculptor("Python3.9!"))
    print(string_sculptor(""))