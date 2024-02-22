n = int(input("Enter range: "))
if n > 2:
    a = [0,1]
    for i in range( 2 , n):
        a.append(a[i-1] + a[i-2])
print(a)