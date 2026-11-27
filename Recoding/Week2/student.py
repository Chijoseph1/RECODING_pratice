def students(student):
    grade = ""
    for value in student:
          total = 0
          val = value[0]
          for scor in value[1:]:
                total += scor       
          score = total / len(value[1:])
        
          if 70<= score <= 100:
                grade = "A"
          elif 60<= score <= 69:
                grade ="B"
          elif 50<= score <= 59:
                grade = "C"
          elif 45<= score <= 49:
                grade = "D"
          elif 40<= score <= 44:
                grade = "E"
          else:
                grade = "F"
          print( f"{val} -> Average: {score:.2f} -> Grade:{grade}")
          
student= [["smauel",80,75,90],
          ["mary",40,35,30],
          ["David",55,60,50],
          ["john",85,70,68]]
students(student)

