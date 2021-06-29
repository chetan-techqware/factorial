def myfunc1(func):
    def wrapper(*args):
        print("my first decor")
        func(*args)
        for x in args:
            if x == "sahil":
                print("Namaste Sahil")
            else:
                pass
        
    return wrapper

def myfunc2(func):
    def wrapper(*args):
        print("my second decor")
        func(*args)
    return wrapper


@myfunc2
@myfunc1
def wish(*args):
    for x in args:
        print(f'Hello {x}')

wish("chetan","sahil","alok","umar")
