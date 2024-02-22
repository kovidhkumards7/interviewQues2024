a = "aabbccaaafffeiii"
b = ""
for i in range(0,len(a)-1):
    c = 0
    b = b + a[i]
    for j in range(i, len(a)-1):
        if a[j] == a[j+1]:
            c += 1
            i += 1
    b = b + str(c)
print(b)