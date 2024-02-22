#input = I_Am_Coder
#output = i.aM.cODER

a = "I_Am_Coder"
a.replace("-",".")
b = ""
for i in a:
    if i == "_":
        b += "."
    elif i.isupper():
            b += i.lower()
    else:
        if i.islower():
            b += i.upper()
print(b)