def whisper_cipher(text: str, shift: int) -> str:
    result = []

    for char in text:
        if "a" <= char <= "z":
            new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            result.append(new_char)
        elif "A" <= char <= "Z":
            new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            result.append(new_char)
        else:
            result.append(char)
    
    return "".join(result)

if __name__ == "__main__":
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("Hello World!", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("ABC123def", 5))
    print(whisper_cipher("", 10))
    print(whisper_cipher("abc", -3))