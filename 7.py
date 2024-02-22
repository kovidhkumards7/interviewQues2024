a = [8,7,2,5,3,1]
k = 10
n = []
for i in a:
    for j in a:
        if i == j:
            continue
        elif i+j  == k:
            n.append([i,j])
print(n)