import pandas as pd
a = []
for i in range(1,11):
    a.append(i)

print(a)

b = {x:x*5 for x in a}
print(b)



df = pd.read_csv("D:\\KOVIDH KUMAR D S\\AzureMLdatasets\\Titanic.csv")



a = df[df["pclass"] == 1]
print(a)
