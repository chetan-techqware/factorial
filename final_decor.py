def decor(func):
    def wrapper(x,y):
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        return func(x,y)
    return wrapper

@decor
def add(x,y):
    b = x + y
    return b

a = add(-10,5)
print(a)




