# def test():
#     print("sample test function")
# test()

# def odd_or_even(n):
#     if(n %2 == 0):
#         print("the number is even")
#     else:
#         print("the number is odd")

# odd_or_even(10)
# odd_or_even(43)

# marks = [45, 47, 50, 48]

def total_marks(name, marks):
    sum = 0
    for mark in marks:
        sum += mark
    print("the total marks for %s is %d" %(name,sum))
    return sum
   

name = input("enter your name:")
count = int(input("how many subjects marks do you want to enter: "))
marks = []
for i in range(count):
    mark = int(input("enter your mark: "))
    marks.append(mark)

# print(marks)

total = total_marks(name,marks)
avg = total/count
print("The average mark is ",avg)
