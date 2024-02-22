a = "reene"
b = []
b.extend(a)
print(b)
b = list(set(b))
print(b)
c = {i:0 for i in b}
print(c)
for i in a:
    c[i] += 1
print(c)