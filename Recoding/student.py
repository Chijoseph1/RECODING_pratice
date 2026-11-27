def student(lists):
    grade =""
    for list in lists:
        value = list[0]
        average = (list[1] + list[2] + list[3]) / 3
        if 70 <= average <= 100:
            grade = "A"
        elif 60 <= average <= 69:
            grade = "B"
        elif 50 <= average <= 59:
            grade = "C"
        elif 45 <=  average <= 49:
            grade = "D"
        elif 40 <=  average <= 44:
            grade = "E"
        else:
            grade = "F"
        print(f"{value}-average:{average:.2f} Grade:{grade}")




students=[
    ["samuel",80,75,90],
    ["bolu",55,60,50],
    ["david",12,12,12],
    ["dav",1,1,12]
]
student(students)
