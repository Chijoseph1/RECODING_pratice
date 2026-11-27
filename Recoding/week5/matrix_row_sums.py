def matrix(numbers):
    result = []
    # for i in numbers:
    #     # i dont know how to use two for loop and store this when i don this am picking the everything 
    #     #  print(row_1+i)
    #     for j in i:
    #         row_1 += j[i]
    # print(row_1)

    for value in numbers:
        # print(value)
        total  = 0
        for i in value:
            total +=  i
        result.append(total)

    output = ""
    for i in range(len(result)):
        output += f"Row{i+1}, total {result[i]}\n"
    return output
    return f"Row 1 total: {result[0]}\nRow 2 total: {result[1]}\nRow 3 total: {result[2]}"

matri = [[2,4,6],[1,3,5],[10,20,30]]
print(matrix(matri))