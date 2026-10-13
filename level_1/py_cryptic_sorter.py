def cryptic_sorter(strings: list[str]) -> list[str]:
    newlist = []

    def vowels(string: str) -> int:
        count = 0
        new_string = string.lower()
        for char in new_string:
            if char in ["a", "e", "i", "u", "o"]:
                count += 1
        return count

    if strings:
        newlist.append(strings[0])

    for i in range(1, len(strings)):
        newlist.append(strings[i])
        
        j = i
        while j > 0 and (len(newlist[j]) < len(newlist[j - 1]) or \
                (len(newlist[j]) == len(newlist[j - 1]) and (newlist[j].lower() < newlist[j - 1].lower())) or \
                (newlist[j].lower() == newlist[j - 1].lower() and vowels(newlist[j]) < vowels(newlist[j - 1]))):
            newlist[j], newlist[j - 1] = newlist[j - 1], newlist[j]
            j -= 1

    return newlist

if __name__ == "__main__":
    print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
    print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
    print(cryptic_sorter(["hello","world","hi","test"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter([""]))