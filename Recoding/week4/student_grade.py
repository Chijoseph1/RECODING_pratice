def student(word):
    average = None
    result = ""
    grade = ""
    value = map(lambda x : (x["name"],x["scores"]),word)
    tupl =(list(value))
    #  still dont understand what that mean 
    for n in tupl:
        result = n[0]
        v = n[1]
        total = 0
        for num in v:
            total += num
        average = total / len(v)
        if average > 70 and average < 100:
            grade = "A"
        elif average > 60 and average < 69:
                grade = "B"
        elif average > 50 and average < 59:
                grade = "C"
        elif average > 45 and average < 49:
                grade = "D"
        elif average > 40 and average < 44:
                grade = "E"
        else:
              grade="F"
      
        answer = print(f"{result} - > Average {average} -> Grade: {grade}")
    return answer
        # still dont know how to usefilter to do  check the greade stuff
        # print(n)
    # result = we[0][0]
        # print(result)



students=[{"name": "sam", "scores":[80,90]},
          {"name":"david","scores":[55,60]}]
student(students)