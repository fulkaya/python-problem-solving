def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    
    for sublist in matrix:
        mid = len(sublist) // 2
        for j in range(mid):
            sublist[j], sublist[-1 - j] = sublist[-1 - j], sublist[j]

    return matrix

if __name__ == "__main__":
    print(mirror_matrix([[1,2,3],[4,5,6]]))
    print(mirror_matrix([[1,2],[3,4],[5,6]]))
    print(mirror_matrix([[7]]))
    print(mirror_matrix([[1,2,3,4]]))
    print(mirror_matrix([[-1,-2],[-3,-4]]))