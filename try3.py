class Vechicle():
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

class Car():
    def __init__(self, color, obj):
        self.color = color
        self.obj = obj

    def display(self):
        print(f"this is a car of {self.obj.brand} brand of type {self.obj.type}")

    def tell(self, o):
        print(f"this is a car of {o.brand} brand of type {o.type}")

v1 = Vechicle("fiat","sedan")
c1 = Car("yellow", v1)

c1.display()
c1.tell(v1)

def hello():
    def decorator(func):
        def wrapper():
            print("hello")
            func()
        return wrapper
    return decorator

@hello()
def sum():
    print(3+6)

sum()