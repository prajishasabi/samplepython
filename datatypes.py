num = 10
print(num)
print(type(num))
num  = 'hai'
print(num)
print(type(num))
num=23.45
print(type(num))
num = 23.8j
print(type(num))
num=2+3j
print(type(num))
name = "prajisha"
print(name)
print(name[1])
print(len(name))
print(name[-1])
print(name[2:])
print("helo "+name)
print(name * 7)
print(name[-7:])
print(name[::-1])
print(name[::2])

numbers = [10,"hello",30,40,50,True,23.87,54.7j,30]
print(numbers)
print(type(numbers))
numbers[1]=65
print(len(numbers))
print(numbers)


fruits = ('apple', 'orange', 'grapes', 'apple')
print(fruits)
# print(fruits[2])
print(type(fruits))
# fruits[1] = 'pineapple'
colors = {'red', 'orange', 'blue', 'green', 'red'}
print(colors)
# print(colors[1])



user = {
    'name': 'raju', 
    'age' : 30,
    'skills' : ['html', 'css', 'js'],
    'job' : {
        'job_title': 'programmer',
        'salary' : 25000
    },
    'gender': True,
    1: 'test'


}
print(user)
# print(type(user))
# print(user['name'])
print(user.values())
# user.clear()
del user['name']


# print(user)


characters = ['a', 'b', 'c', 'd']
dict1 =  dict. fromkeys(characters,1)
print(dict1)



marks = [35, 40, 50, 48, 49]
print(len(marks))
print(list(marks))
print(sum(marks))
print(min(marks))
print(max(marks))
print(list(reversed(marks)))
print(sorted(marks))



# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # car.pop("model")
# # print(car)
# car.update({"color": "White"})
# print(car)
# # x = car.values()
# # print(x)
# # x = car.items()
# # print(x)
# # x = car.copy()
# # print(x)
# x = car.get("model")
# print(x)