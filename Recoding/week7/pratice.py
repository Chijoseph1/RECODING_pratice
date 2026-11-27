matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
    ]

def mat(m):
    # size = max(len(m), len(m[0]))
    # while len(m) < size:r+1
    #     m.append("-" for _ in range(m[0]))

    # while len()
    for r in range(len(m)):
        for c in range(len(m[0])):
            if r < c:
                m[r][c], m[c][r] = m[c][r], m[r][c]
    return m

print(mat(matrix))
