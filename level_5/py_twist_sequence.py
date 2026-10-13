def twist_sequence(arr: list[int], k: int) -> list[int]:
    
    if not arr:
        return []

    num = k % len(arr)
    first = len(arr) - num
    result = []

    for i in range(num):
        result.append(arr[-num +i])
    
    for i in range(first):
        result.append(arr[i])
    
    return result

# second solution

    # if not arr:
    #     return []

    # k = k % len(arr)

    # return arr[-k:] + arr[:-k]

if __name__ == "__main__":
    print(twist_sequence([1,2,3,4,5], 2))
    print(twist_sequence([1,2,3], 1))
    print(twist_sequence([1,2,3,4], 0))
    print(twist_sequence([1,2,3], 5))
    print(twist_sequence([], 3))