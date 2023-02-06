# try:
#     n1= int(input("enter first number:"))
#     n2 = int(input("enter second number:"))
#     n3 = n1/n2
#     print("the result is ", n3)
# except ZeroDivisionError:
#     print("cant divide a number by zero")
# except ValueError:
#     print("cant input string characters")


# except Exception as e:
#     print("an exception occured")
#     print(e)

# else:
#     print("program completed without any exceptions")
# finally:
#     print("program completed")


try:
    fh=open('testfile.txt','r')
    fh.write("this is the test file for exception handling")
    fh.close()
except FileNotFoundError:
    print("error!cant find or read data")
else:
    print("written content in the file successfully")
finally:
    print("program execution completed")