a = [456,4,87,6541,56,746,541,32,41,564,132,1,53,4,531,54,54,746,41,32]
b = list(set(a))
c = {x:0 for x in b}

for i in a:
    if i in b:
        c[i] += 1
for i in c.keys():
    if c[i] > 1:
        print(i)