# n = int(input("enter a number "))
# if(n % 2 == 0):
#     print("the number is even")

# else:
#     print("the number is odd")  
#     n = int(input("enter a number "))

# n = int(input("enter a number "))
# if(n > 0):
#     print("the number is positive")
# elif(n == 0):
#     print("the number you entered is zero")
# else:
#     print("the number is negative")  

n1 = int(input("enter your first number"))
n2 = int(input("enter your second number"))
n3 = int(input("enter your third number"))
if(n1 > n2):
    if(n1 > n3):
        print("the greatest number is ", n1)
    else:
        print("the greatest is ", n3)
elif(n2 > n3):
    print("the greatest number is ", n2)
else:
    print("the greatest number is ", n3)
    # print("the number is %d, %d" %(n3,n2))





