a = "nitin"
b = a[::-1]
print(a==b)
c = ""
for i in range(len(a),0,-1):
    c += a[-i]
print(c==b)

a = 4165
b = a
s = 0
while a > 0:
    t = a % 10
    s = s * 10 + t
    a = a // 10
print(s==b)