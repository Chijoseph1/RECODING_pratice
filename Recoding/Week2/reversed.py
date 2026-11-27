# def reversed(val):
#     result= ""
#     reversed_last = ""
#     reversed_split = ""
#     reversed_val = ""
#     if val.startswith(" ")and val.endswith(" "):
#         reversed_val = val[::-1]
#         reversed_split  = reversed_val.split()
#         reversed_last = reversed_split[::-1]
#         result = " " + " ".join(reversed_last) + " "
#     else:
#           reversed_val = val[::-1]
#           reversed_split  = reversed_val.split()
#           reversed_last = reversed_split[::-1]
#           result = " ".join(reversed_last)
#     return result 
  
# def reverse(val):
#     vl = []
#     v = ""
#     reverse_i= val.split(" ")
#     for i in range(len(reverse_i)-1,-1,-1) :
#         v = val[i]
#         vl.append(reverse_i[i])
#     return  " ".join(vl)

    
for i in range(8):
    print(i)
# print(reverse(" This is an example! "))