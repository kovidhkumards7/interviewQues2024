a = [456,4,87,6541,56,746,541,32,41,564,132,1,53,4,531,54]
a = list(set(a))

for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]

print(a)