def check_palindrome(a):
    n=a.lower()
    first = 0
    second =len(n)-1
    
    while first < second:
        if n[first] != n[second]:
            return False   
        first+= 1
        second-=1
    return True
    
        
y=check_palindrome("Snns")
print(y)