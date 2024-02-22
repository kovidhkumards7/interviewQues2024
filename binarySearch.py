n = int(input("Enter num to search: "))
a = [456,4,87,6541,56,746,541,32,41,564,132,1,53,4,531,54]
a = list(set(a))
a.sort()

low = 0
high = len(a) - 1
flag = False

while low <= high and not flag:
    mid = int((low+high)/2)
    if a[mid] == n:
        flag = True
    elif a[mid] > n:
        high = mid - 1
    elif a [mid] < n:
        low = mid + 1

if flag:
    print(f"ele found at {mid+1} location")
else:
    print("not found")
