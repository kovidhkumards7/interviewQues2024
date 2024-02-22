# Define a generator function that yields the squares of numbers
def square_generator(n):
    for i in range(n):
        yield i**2

# Use the generator to get the squares of numbers up to 5
gen = square_generator(5)

# Print the squares using a for loop
for s in gen:
    print(s)
print("888888888888888888")
def gena(n):
    for i in range(0,n):
        yield n**2


a = gena(5)

print(a)
for i in a:
    print(i)
