def anagram(word1,word2):
    # dic1 ={}
    # dic2 = {}
    # for val in word1.lower():
    #     if val in dic1:
    #         dic1[val] += 1
    #     else :
    #         dic1[val] = 1
    # for val in word2.lower():
    #     if val in dic2:
    #         dic2[val] += 1
    #     else :
    #         dic2[val] = 1

    # if dic1.keys() == dic2.keys():
    #     print("Anagram")
    # else:
    #     print("Not anagram")
    if word1  in word2:
        print("A")
    else:
        print("b")

anagram("silent","listen") 

