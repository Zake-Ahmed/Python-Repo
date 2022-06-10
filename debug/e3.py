import pdb
def is_prime(x):
    #pdb.set_trace()
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x+1):
            if x % n == 0 and x != n:
                return False
            
    return True
list1=[2,3,4,5,6,7,15,20,25]
for i in list1:
    print(is_prime(i))