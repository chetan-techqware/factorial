import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("time : ",total)
        return rv
    return wrapper

@timer
def test():
    for x in range(10000):
        pass



test()
