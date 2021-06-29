# 1
# import sys
# def gen(n):
#     for i in range(n):
#         yield i**2

# x = [i**2 for i in range(10000)]
# g = gen(10000)

# print(sys.getsizeof(x))
# print(sys.getsizeof(g))

# #2
# def create_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result
# x = create_cubes(5)
# print(x)

#3
# def fibo(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b, a+b

# for x in fibo(10):
#     print(x)

#4
# def gensquares(n):
#     for i in range(n):
#         yield i**2

# g = gensquares(10)
# for x in g:
#     print(x)

#5
# import random
# def rand_num(low, high, n):
#     for i in range(n):
#         yield random.randint(low,high)

# for x in rand_num(1,10,12):
#     print(x)

#6
# s = "hello"
# g = iter(s)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
mynums = [1,2,3,4,5,6,7,8,9]
num = (i**2 for i in mynums)
mylist = []
for i in num:
    mylist.append(i)

print(mylist)








