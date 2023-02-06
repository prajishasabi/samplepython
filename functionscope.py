# x = 10
# y = 20
# def scopefunction():
#     global y
#     y+=10
#     print("value of x and y is " ,x,y)
# scopefunction()
# print("value of x and y is " ,x,y)



# x = 10
# y = 20
# def scopefunction():
#     x=1
#     y=2
#     print("value of x and y is " ,x,y)
# scopefunction()
# print("value of x and y is " ,x,y)


def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))



