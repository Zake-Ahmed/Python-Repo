name = input('Please input your name ')
homeWork= int(input('Please input your homework score '))
assesment = int(input('Please input your assesment score '))
finalExam = int(input('Please input your final exam score '))

def program(userName, home,ass,exam):
    userName = str(userName)
    finalMark = home+ass+exam
    finalPer= (finalMark/175)*100
    if finalPer>=90:
        grade = 'A'
    elif finalPer>=70:
        grade = 'B'
    elif finalPer>=40:
        grade = 'C'
    else:
        grade = 'U'
    
    return f'{userName} got and final score of {int(round(finalPer))}% with a grade of {grade}'

print(program(name,homeWork,assesment,finalExam))
