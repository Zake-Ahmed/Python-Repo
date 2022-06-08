n = int(input('Please input the grid number '))

def grid(number):
    numberList = ""
    for i in range(1,number+1):
        
        for j in range(1,number+1):
            add = i*j
            numberList = numberList + str(add) + "\t"
        numberList = numberList + "\n"
    return numberList

print(grid(n))