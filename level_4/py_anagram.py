def anagram(s1: str, s2: str) -> bool:
    clean_s1 = s1.lower().replace(" ", "")
    clean_s2 = s2.lower().replace(" ", "")
        
    return sorted(clean_s1) == sorted(clean_s2)

if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("Triangle", "Integral"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))
    print(anagram("", ""))
    print(anagram("abc", "abcc"))
