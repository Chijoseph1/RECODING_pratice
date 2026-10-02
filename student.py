def student(word):
    vl = ""
    score = None
    grade = ""
    # i dont know how to loop through a lsit of dictionaries
    #  i dont know how dictionaries really work
    for val in word:
        # how does me to
        for key,value in val.items():
            if key == "name":
                vl = value
            if key == "scores":
                score = value
                # i dont know how to use rounding and round up figure and what the difference between those 2
        b = sum(score)/ len(score)
        if b > 70 and b < 100:
            grade = "A"
        elif b > 60 and b < 69:
            grade = "B"
        elif b > 50 and b < 59:
            grade = "C"
        elif b > 45 and b < 49:
            grade = "D"
        elif b > 40 and b < 44:
            grade = "E"
        else:
            grade = "F"
        print(f"{vl} -> {b:.2f} -> {grade}")
    #  how will i do that operation 


word = [{"name": "Sam", "scores": [80, 90]}, {"name": "David", "scores": [55, 60]}]

(student(word))