def inter(s1: str, s2: str) -> str:
    result = []

    for char in s1:
        if char in s2 and char not in result:
            result.append(char)
    
    return "".join(result)

if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))