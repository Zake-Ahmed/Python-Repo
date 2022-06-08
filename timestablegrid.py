n = int(input('Please input the grid number '))

def grid(number):
    numberList = []
    numbers = []
    for i in range(1,number+1):
        
        for j in range(1,number+1):
            add = i*j
            numbers.append(str(add))
        numberList.append(numbers)
        numbers=[]
    
    return numberList

for z in range(n):
    print(f'{"  ".join(grid(n)[z])}')