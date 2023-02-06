# def product_details(item,price):
#     print("%s cost %d" %(item,price))


# product_details("soap",35)

# keyword argument , default arguments


# def product_details(item,price, discount = 20):
#     print("%s cost %d discount %d" %(item,price,discount),"%")


# product_details(price=35,item= "soap")
# product_details(price=235,item= "shampoo", discount=30)

# variable length argument

# def product_details(item, *components):
#     print("components of %s are:" %(item))
#     for component in components:
#         print("- ",component)
# product_details("computer", "mouse","keboard", "monitor", "cpu")


# variable length keyword arguments

def product_details(item, **properties):
     print("properties of %s are:" %(item))
     print(properties.items())
     for key, value in properties.items():
        print("- %s is %s " %(key,value))
     print(properties)

product_details("soap",price="45", brand="lux" ,flavour="rose")
    
