p1 = int(input("enter the price: "))
p2 = int(input())
p3 = int(input())
p4 = int(input())
prices = [p1, p2, p3, p4]
total_bill = 0
for i in range(len(prices)):
    total_bill = total_bill+prices[i]
if(total_bill>10000):
    print("Your total  bill is ",total_bill)
    print("you have got 25% discount")
    discount = (total_bill*25)/100
    discount_bill = total_bill-discount
    print("after discount your total bill is ",discount_bill)
elif(total_bill>5000):
    print("Your total  bill is ",total_bill)
    print("you have got 18% discount")
    discount = (total_bill*18)/100
    discount_bill = total_bill-discount
    print("after discount your total bill is ",discount_bill)
elif(total_bill>2000):
    print("Your total  bill is ",total_bill)
    print("you have got 12% discount")
    discount = (total_bill*12)/100
    discount_bill = total_bill-discount
    print("after discount your total bill is ",discount_bill)
else:
    print("you are not eligible for any discount!")
    print("your  total bill amt is ",total_bill)


    
