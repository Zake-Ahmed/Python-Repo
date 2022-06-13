x= int(input('input number '))

def factorial(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x

print(f'The factorial of {x} is {factorial(x)}')
