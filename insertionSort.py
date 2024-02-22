a = [456,4,87,6541,56,746,541,32,41,564,132,1,53,4,531,54]
a = list(set(a))

for i in range(1,len(a)):
    j = i
    while a[j-1] > a[j] and j > 0:
        a[j-1],a[j]=a[j],a[j-1]
        j -= 1

print(a)