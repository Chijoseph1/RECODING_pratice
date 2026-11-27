def consecutive_number_analse(num):
    i=0
    count = 0
    while i < len(num)-1:
        print(num[i+1])
        if num[i+1] > num[i]:
            count+=1
            i+=1
        else:
            i+=1
    
    return count
num = [1, 2, 3, 7, 5]
print(consecutive_number_analse(num))