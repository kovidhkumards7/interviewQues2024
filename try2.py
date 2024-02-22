def Hello():
    def decorator(func):
        def wrapper():
            print("Hello there!")
            func()
        return wrapper
    return decorator

@Hello()
def Sum():
    print("The sum of 5 and 6 is:", 5 + 6)

Sum()