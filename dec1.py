def dec(func):
    def wrapper():
        print("decorator function")
        print(func)
    return wrapper

x = dec("ramleela")
print(x)
x()



# def sim():
#     print("simple function")

# x = dec(sim)


