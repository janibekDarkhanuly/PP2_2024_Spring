
def filter_prime(n):
    if n == 1:
        return False
    elif n>1:
        for i in range(2,n):
            if(n%i) == 0:
                return False
    return True
n = input()
arr = n.split()
for i in range(0,len(arr)):
    if(filter_prime(int(arr[i])) == True):
        print(int(arr[i]))
         
                
    