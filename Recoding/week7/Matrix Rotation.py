def matrix(a,b):
    
    print(len(a),len(b))
    if len(b) != len(a[0]):
        return "error"

a = [[1,2]]
b = [[5, 6], [7, 8]]
print(matrix(a,b))