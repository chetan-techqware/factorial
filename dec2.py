def func(f):
    def wrapper(*args,**kwargs):
        print("Started")
        rv = f(*args,**kwargs)
        print("Ended")
        return rv

    return wrapper
@func
def func2(x,y):
    print(x)
    return y


@func
def func3():
    print("i am func 3")

x = func2(5,6)
print(x)



# func2 = func(func2) is equals to @func
# func3 = func(func3) is equals to @func
# func3()

