n = int(input("Enter num: "))
if n > 2:
    count = 0
    for i in range(2,n-1):
        if n % i == 0:
            count += 1
            break
    if count == 0:
        print("prime")
    else:
        print("not prime")
else:
    print("enter number > 2")

def primeOrNot(n:int):
    count = 0
    for i in range(2,n-1):
        if n % i == 0:
            count += 1
            break
    return count
for i in range(100, 200):
    if primeOrNot(i) == 0:
        print(i," is prime number")