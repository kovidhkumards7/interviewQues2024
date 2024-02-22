a = "naina"
b = "reene"
a1 = []
b1 = []
a1.extend(a)
b1.extend(b)
a1 = list(set(a1))
b1 = list(set(b1))
c = []
for i in a1:
    if i in b1:
        c.append(i)

print(c)