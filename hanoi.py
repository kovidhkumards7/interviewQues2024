n = int(input("Enter num: "))
def hanoi(n,a="1st tower",b="2nd tower",c="3rd tower"):
    if n == 1:
        print(f"move {n}th disc from {b} to {c}")
    else:
        hanoi(n-1,a,c,b)
        print(f"move {n}th disc from {b} to {c}")
        hanoi(n-1,b,a,c)
hanoi(n)