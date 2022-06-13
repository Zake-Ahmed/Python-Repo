names = []
i=0
while len(names)<5:
    name1 = input('please input your name: ')
    names.append(name1)

while i<5:
    print(f'{names[i]}, is awesome!')
    i+=1