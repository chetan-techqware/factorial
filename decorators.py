def smart_div(func):
    def wrapper(a,b):
        print(f"we are dividing {a} with {b}")

        if b == 0:
            print("oops..cant divide")
        else:
            return func(a,b)

    return wrapper

@smart_div
def div(a,b):
    return a/b

x = div(100,0)
print(x)

