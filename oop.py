# OOP is a paradigm: way to structure our code
# class BigObject:
#     #code
#     pass


# obj1 = BigObject() #instantiate
# obj2 = BigObject() #instantiate

# print(type(obj2))

# Creating a class

# class PlayerCharacter:
#     #Class object Attribute: it doesnt change accross instances
#     membership = True
#     def __init__(self, name='anonymous', age=0): #constructor/init function
#         #to check if player is a member i.e
#         # if (self.membership):
#         if (age > 18):
#             #class attributes: are dynamic and specific to each object
#             self.name = name
#             self.age = age
#             # self.greet = greet'hello'
#         else:
#             print(f'You are {age} years old, you\'re not old enough')
#             return


#     def shout(self):
#         print(f'My name is {self.name}')
#         print('done')

#     # def run(self):
#     #     print('Running')

# player1 = PlayerCharacter('Tom', 10,)
# # print(player1.membership)
# # print(player1.age)
# # print(player1.run())
# print(player1.shout())

# EXERCISE
# Exercise Cats Everywhere

# Given the below class:

# class Cat:
#     species = 'mammal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# #Answers:
# # 1 Instantiate the Cat object with 3 cats.
# cat1 = Cat('cat1', 5)
# cat2 = Cat('Cat2', 7)
# cat3 = Cat('Cat3', 3)


# # 2 Create a function that finds the oldest cat.
# def oldest_cat(*args):
#     return max(args)


# # 3 Print out: "The oldest cat is x years old.".
# # x will be the oldest cat age by using the function in #2
# print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')


# class PlayerCharacter:
#     membership = True
#     def __init__(self, name, age):
#         if (age > 18):
#             self.name = name
#             self.age = age
#         else:
#             print(f'You are {age} years old, you\'re not old enough')
#             return

# def shout(self):
# print(f'My name is {self.name}')
# print('done')

# DECORATORS : @classmethod or @staticmethod
# Is a class method we can use without instantiating the object
# we use it where we do care about class state i.e attributes or to change them
# @classmethod
# def adding_things(cls, num1, num2): # cls means class/ same as self in above
#     # return num1 + num2
#     return cls('Bin',  num1 + num2)

# @staticmethod #we use it where we dont care about class state i.e attributes
# def adding_things2( num1, num2): # we dont have access to cls parameters here
#     # return num1 + num2
#     return 'Bin',  num1 + num2


# player1 = PlayerCharacter('Tom', 20)
# player3 = PlayerCharacter.adding_things( 21, 10)
# print(player3.age)
# print(player1.adding_things( 4, 1)) #instantiate with objects
# print(PlayerCharacter.adding_things( 21, 10)) #without instantiate palyer object

# 4 PILLARS OF OOP
# ENCAPSULATION: the idea is the ability to bind different
# characters into a single class of objects
# class PlayerCharacter:
#     membership = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print('run')

#     def shout(self):
#         print(f'I am {self.age} years old')

#     def speak(self):
#         print(f'My name is {self.name} and i am {self.age} years old')
#         print('done')
#         return


# player1 = PlayerCharacter('Tom', 22)
# print(player1.speak())


# ABSTRACTION: the idea is hiding information
# and giving access to only whats neccessary
# only what the user/machine/programmer is interested in
# that it gives access to
# e.g
# print(len('Hello dear')) #we don't need to know how it did it because
# we only care to see want we want so the 'how' is abstracted from us

# PRIVATE Vs PUBLIC
# PRIVATE: we use "_" as a convention to set private attributes
# so that someone cannot modify it
# class PlayerCharacter:
#     membership = True

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def run(self):
#         print('run')

#     def speak(self):
#         print(f'My name is {self.name} and i am {self.age} years old')
#         print('done')
#         return


# player1 = PlayerCharacter('Tom', 22)
# print(player1.speak())


# INHERITANCE: allows new objects to take the properties of
# existing ones e.g
# class User():
#     def sign_in(self):
#         print('logged in')
#         return


# class Wizard(User):  # inherited the User class
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')


# class Archer(User):  # inherited the User class
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left- {self.num_arrows}')


# wizard1 = Wizard('Merlin', 50)  # instantiating
# arher1 = Archer('Robbin', 100)
# print(wizard1.sign_in())
# print(wizard1.attack())
# print(arher1.sign_in())
# print(arher1.attack())


# # isinstance(instance, Class): bulit in function to check instances
# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, User))
# print(isinstance(wizard1, object))  # in python everything is an object


# POLYMORPHISM:  idea to have diffs forms/many(poly) forms(morphism)
# diff objs classes can share methods names based on what objects calls them
# class User():
#     def sign_in(self):
#         print('logged in')
#         return

#     def attack(self):
#         print('do nothing')


# class Wizard(User):

# def __init__(self, name, power):
#     self.name = name
#     self.power = power

# def attack(self):
#     User.attack(self)  # allows User to run attack as well
#     print(f'attacking with power of {self.power}')


# class Archer(User):  # inherited the User class
# def __init__(self, name, num_arrows):
#     self.name = name
#     self.num_arrows = num_arrows

# def attack(self):
#     print(f'attacking with arrows: arrows left- {self.num_arrows}')


# wizard1 = Wizard('Merlin', 50)
# arher1 = Archer('Robbin', 100)


# print(wizard1.attack())
# NOw to use polymorphism, we can create a new function
# def player_attack(char):
#     char.attack()


# same function is used to call attack with diff objects class
# player_attack(wizard1)
# # same here
# player_attack(arher1)


# OR: another way

# for char in [wizard1, arher1]:
#     char.attack()


# EXERCISES solutions
# class Pets():
#     animals = []

#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # 1 Add nother Cat


# class Thonny(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# # 2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = []

# cat1 = Simon('Simon', 10)
# cat2 = Sally('Sally', 15)
# cat3 = Thonny('Thonny', 6)

# my_cats.append(cat1)
# my_cats.append(cat2)
# my_cats.append(cat3)

# # OR
# # my_cats = [Simon('Simon', 10), Sally('Sally', 15), Thonny('Thonny', 6)]
# # print(my_cats)

# # 3 Instantiate the Pet class with all your cats use variable my_pets
# my_pets = Pets(my_cats)

# # 4 Output all of the cats walking using the my_pets instance
# print(my_pets.walk())


# SUPER()


# OBJECT INSTROSPECTION: ability to check the objects at run time
# dir()


# Dunder Methods:
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name': 'Yoyo',
#             'has_pets': False,
#         }

#     def __str__(self):
#         return f"{self.color}"

#     def __len__(self):
#         return 5

#     def __del__(self):
#         return "deleted"

#     def __call__(self):
#         return ('yes??')

#     def __getitem__(self, i):
#         return self.my_dict[i]


# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure())
# print(action_figure['name'])


# Exercise Extending List
# class SuperList(list):

#     def __len__(self):
#         return 1000


# super_list1 = SuperList()
# print(len(super_list1))

# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(SuperList, list))
# print(issubclass(list, object))


# MRO: https://www.srikanthtechnologies.com/blog/python/mro.aspx


# FUNCTIONAL PROGRAMMING
# Pure Functions
# https://github.com/aneagoie/ztm-python-course-exercises

# from functools import reduce

# # 1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']


# def capitalize(string):
#     return string.upper()


# print(list(map(capitalize, my_pets)))


# # 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]

# print(list(zip(my_strings, sorted(my_numbers))))


# # 3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]


# def is_smart_student(score):
#     return score > 50


# print(list(filter(is_smart_student, scores)))


# # 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# def accumulator(acc, item):
#     return acc + item


# print(reduce(accumulator, (my_numbers + scores)))


# LAMBDA
# Square
# my_list = [5, 4, 3]

# print(list(map(lambda item: item*item, my_list)))

# # List Sorting
# a = [(0, 2), (4, 3), (9, 9), (10, -2)]

# a.sort(key=lambda x: x[1])
# print(a)


# COMPREHENSION
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
# print(duplicates)


# DECORATORS:
# http://github.com/aneagoie/ztm-python-course-exercises/blob/main/4.%20Advanced%20Python/7-ExerciseDecorators.py

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     "name": "Sorna",
#     "valid": True,  # changing this will either run or not run the message_friends function.
# }


# def authenticated(fn):
#     # code here
#     def wrapper(*args, **kwargs):
#         if args[0]["valid"]:
#             return fn(*args, **kwargs)
#         else:
#             return print("invalid user")

#     return wrapper


# @authenticated
# def message_friends(user):
#     print("message has been sent")


# message_friends(user1)


# Errors in Python
# https://docs.python.org/3/library/exceptions.html


# GENERATORS
# generators.

# generators are much more performant than lists. (i.e range > list in performance.)

# So generators are really, really useful when calculating large sets of data.

# from time import time

# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, *kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper

# @performance
# def long_time():
#     print('1')
#     for i in range(1000000): #it finishes after.
#         i*5

# long_time()
# print()

# @performance
# def long_time2():
#     print('2')
#     for i in list(range(1000000)): #it took longer.
#         i*5

# long_time2()
# print()


# generator under the hood
# def special_for(iterable):
#   iterator = iter(iterable)
#   while True:
#     try:
#       iterator*5
#       next(iterator)
#     except StopIteration:
#       break


# class MyGen:
#   current = 0
#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
#     MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration

#   def __iter__(self):
#     return self

#   def __next__(self):
#     if MyGen.current < self.last:
#       num = MyGen.current
#       MyGen.current += 1
#       return num
#     raise StopIteration

# gen = MyGen(1,100)
# for i in gen:
#     print(i)


# def fib(number):
#     n1 = 0
#     n2 = 1
#     for i in range(number):
#         yield n1
#         temp = n1
#         n1 = n2
#         n2 = temp + n2


# for x in fib(10000):
#     print(x)


# A journey of 100+ simple yet interesting problems which are explained, solved, discussed in different pythonic ways

# https://github.com/darkprinx/break-the-ice-with-python


import sys

from random import randint

random_number = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        number = int(
            input('Please choose a number that falls between those two you just chose: '))
        if number >= int(sys.argv[1]) and number <= int(sys.argv[2]):
            if number == random_number:
                print("You're a genius!")
                break
    except ValueError:
        print("Please enter a number")
        continue
