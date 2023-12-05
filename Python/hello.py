# start python

# print('hi')
# print('Voktho')
# print('&'*5)
# x = 5
# x = 10
# name = 'panku'
# is_published = False
# print('x:')
# print(x)
# print(name)

# #receiving input
# name=input('Whats your name? ')
# colour=input('Fav Colour? ')
# print('I am ' + name)
# print(name + ' likes ' + colour)

# #Type Conversion
# birth_year=input('Birth Year:')
# print(type(birth_year))
# age=2021- int(birth_year)  #for str2int
# print(age)
# print(type(age))
# print('You are '+ str(age) + ' years old') #for int2str
#

##strings
#
# case1= 'Python for "Beginners"'
# case2="Python's course for Beginners"
# print(case1)
# print(case2)
# #for multi line
# case3='''
# Hi Voktho,
# How are you?
# '''
# print(case3)
#
# print(case1[0])
# print(case1[-2]) #from the ending of the string
# print(case1[0:])
# print(case1[0:3])#excluding 4th char
# print(case1[:3])
# print(case1[:])
# print(case1[1:-1])

# Formated String

# first_name = input("what's your First name? ")
# last_name= input("what's your last name? ")
# new_msg=first_name +' ['+last_name+'] is a student'
# print(new_msg)
# msg=f'{first_name} [{last_name}] is a student'
# msg2=f'{first_name} {last_name}'
# print(msg2)

##string method

# yp='It is an exciting match'
# print(len(yp)) ##using len , we can calculated no of character in a string
# print(yp.upper()) ##method
# print(yp.lower())
# print(yp.find('e'))
# print(yp.find('match'))
# print(yp.replace('match','day'))
# print('exciting' in yp) ##Boolean true or false
# print('day' in yp)

##arithmetic
# a=int(input())  ##take input as a string then change the type to int and calculated
# b=int(input())
# c=a+b
# print(str(c))

# x=2
# p=2
# x=x+3
# p += 3
# print(x)
# print(p)
# print(x*2)
# print(x**2) #power
# print(x/2)
# print(x//2) #only floor

##mathfunction
# import math
# print(math.ceil(3.9))
# print(math.remainder(4,5))
# print(math.fmod(4,5))

##if_statement

# is_day=False
# is_night=False
# if is_day:
#     print('wake up')
# elif is_night:
#     print('go to bed')
# else:
#     print('chil')

##logicalOperator
# is_happy=True
# is_active=False
# # if is_happy and is_active:
# #     print("work")
# # elif is_happy or is_active:
# #     print('play games')
#
# if is_happy and not is_active:    #and not makes the is_active variable true
#     print("work")

##comparison

# import math
#
# x =int(input('Number: '))
# if math.remainder(x, 2) == 0:
#     print('Even')
# else:
#     print('Odd')
#
# if x>0:
#     print('positive')
# else:
#     print('Negative')

# name=input("What's your name: ")
# if len(name)<3:
#     print('Name must be at least 3 characters')
# elif len(name)>50:
#     print('name can be a maximum of 50 characters')
# else:
#     print(f'Perfect :{name}')

##weight converter


# weight=int(input('Enter your weight: '))
# unit=input('(L)bs or (K)g: ')
# if unit.upper()=='L':
#     weight *= 0.45
#     print(f'You are {weight} Kilos')
# elif unit.upper() == 'K':
#     weight /= 0.45
#     print(f'You are {weight} pounds')


##while_loop

# i=1
# while i<=7:
#     print('*' *i)
#     i+=1


# assignment1::
##Number guessing


# Guess_counter=1
# Guess_limit=3
# while Guess_counter<=Guess_limit:
#     secret_number=int(input('Guess: '))
#     if secret_number==9:
#         print('You won!')
#         break
#     Guess_counter= Guess_counter + 1
#
# else:
#     print('You failed')


##asssignment2:
##car_driving

# command=""
# print(''' Help:
# start - to start the car
# stop - to stop the car
# quit - to quit
# ''')
# started=False
# while True:
#     command = input('>').lower()
#     if command== "start":
#         if started:
#             print('Car already started!!')
#         else:
#             started=True
#             print('Car started...lets go!!')
#     elif command== "stop":
#         if not started:
#             print('Car already stopped!')
#         else:
#             started=False
#             print('Car stopped.')
#     elif command == "quit":
#         print('Finished!!')
#         break
#     else:
#         print('Wrong command!!')


##for loops

# for item in 'Panku':
#     print(item)
#
# for item in ['panku','voktho','das']:
#     print(item)
# for i in [1,2,3]:
#     print(i)
# for item in range(13):
#     print(item)
# for item in range(2,12):
#     print(item)
# for i in range(2,15,3):
#     print(i)


##assignment

# for i in range(1,4)
# prices=[20,30,40]
# cost=0
# for item in prices:
#     cost+=item
# print(f"Total cost: {cost}")

##nested loop
# for x in range(4):
#     for y in range(4):
#         print(f'({x},{y})')

##assignmemt (create F)

# n=[5,2,5,2,2]
#
# # for i in n:
# #     print('x'*i)  ##shortcut
#
# for x_counts in n:
#     output=''
#     for counts in range(x_counts):
#         output+='x'
#     print(output)


##List

# name=['voktho','panku','santona','kamona']
# print(name)
# print(name[0])
# print(name[2])
# print(name[-1])
# print(name[1:])
# print(name[1:3])
# print(name[:3])
#
# name[0]='das' #replace
# print(name)

##assignmet(max number)

# numbers=[29,3,100,224,22,45,32]
# max=0
# for x in numbers:
#     if x>max:
#         max=x
# print(max)


##2DList

# a=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(a[2])
# print(a[1][2])
#
# a[0][0]=23 #replace
# print(a)

# for row in a:
#     for item in row:
#         print(item)

##list methods

# b=[4,6,2,9,7,9]
# b.append(20) #add new item at the end of a list
# print(b)
# b.insert(1,13)  #add new item at any position of a list
# print(b)
# b.remove(6) ##remove the integer 6  from the list
# print(b)
# b.clear()
# print(b)
# b.pop()  #delete last item
# print(b)
# print(b.index(9))  #index of a item
# print(9 in b) #checking the existense
# print(b.count(9))   #count how many times a item occurs in a list
# c=b.copy()
# print(c)
# b.sort()  #sort the list
# print(b)
# b.reverse()
# print(b)


##take input of a list

# numbers=[int(num) for num in input('Numbers: ').split()]
# print(numbers)
#
# char=[ch for ch in input("String: ").split()]
# print(char)

# n=int(input("No of item: "))  ##another process
# num_list=[]
# for x in range(0,n):
#     num_list.append(int(input('Numbers: ')))
# print(num_list)

##assignment( remove a duplicate from list)

# x=[23,4,6,7,23,6,9,9,2,7]
# new_x=[]
# for item in x:
#     if item not in new_x:
#         new_x.append(item)
# print(new_x)

##tuples (like list but can't modify)

# numbers=(1,4,6)
# print(numbers[1])
# print(numbers.count(6))
# print(numbers.index(6))
## numbers[0]=5  #can not change the value

##unpacking

# a=[1,4,6] ##instead of x=a[0],y=a[1],z=a[1]
# x,y,z=a
# print(f'{x},{y},{z}')
# v=(2,4,5)
# r,s,t=v
# print(f'{r},{s},{t}')
##print(sum(a))


##Dictionaries

# student={
#     'name':'Voktho Das',
#     'age': 21
# }
#
# print(student['name'])
# print(student.get('name'))
# print(student.get('birthday'))
# print(student.get('birthday','Jan 4 2000'))
# print(student)
# student['name']='Panku Das'  ##update the dictionaries
# student['weight']=80
# print(student)

##assignments(phone num)

# num=input('Phone: ')
# digits={
#     '0':'zero',
#     '1':'One',
#     '2':'Two',
#     '3':'Three',
#     '4':'Four',
#     '5':'Five',
#     '6':'Six',
#     '7':'Seven',
#     '8':'Eight',
#     '9':'Nine'
# }
# output=''
# for ch in num:
#     output+=digits.get(ch) + ' '
# print(output)

##emojiConverter

# message=input('> ')
# words=message.split(' ')
# emojis={
#     ':)':'😊',
#     ':(':'😥'
# }
# output=''
# for word in words:
#     output+=emojis.get(word,word)+' '  ##if the key is absent in dictionary then use this word as default
# print(output)


##function & parameters

# def greet_user(first_name,last_name):
#     print(f'Hi {first_name} {last_name}')
#     print('welcome')
#
# f=input('first name: ')
# l=input('last name: ')
# greet_user(f,l) ##positional argument

##keyword argument

# def calc_profit(quantity,sales_price,cost_price,discount):
#     total_profit=(sales_price -cost_price)*quantity-discount*(sales_price*quantity)
#     print(f'Profit : TK {total_profit}')
#
#
# calc_profit(sales_price=100,quantity=250,cost_price=60,discount=0.1)  ##we can use keyword argument after positional argument.


##return_statement
# def square(num):
#     return num*num
#
# x=int(input('Number: '))
# result=square(x)
# print(result)

##assignment(function of emoji_converter)

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ':)': '😊',
#         ':(': '😥'
#     }
#     output = ''
#     for word in words:
#         output += emojis.get(word, word) + ' '
#     return output
#
# message=input('> ')
# result=emoji_converter(message)
# print(result)

###Exceptions

# try:
#     age=int(input('Age: '))
#     income=100000
#     risk=income/age
#     print(age)
# except ZeroDivisionError:
#     print('Age can not be Zero')
# except ValueError:
#     print('Invalid Value')
#


##class

# class Point:
#     def move(self):
#         print('move')
#     def draw(self):
#         print('draw')
#
# point1=Point()  #object
# point1.move()
# point1.x=5   #set atribute
# print(point1.x)

##constructor

# class Point:
#     def __init__(self,x,y):      3CONSTRUCTOR
#         self.x=x                 #initialize the atribute
#         self.y=y
#     def move(self):
#         print('move')
#     def draw(self):
#         print('draw')
#
#
# point2=Point(10,20)
# print(point2.x)


##assignment

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         print(f'Hi,I am {self.name}')
#
#
# name=input('Name: ')
# person1=Person(name)
# person1.talk()


##Inheritance  # don,t repeat our code

# class Mammal:
#     def walk(self):
#         print('walk')
#
#
# class Dog(Mammal):
#     def bark(self):
#         print('Bark')
#
#
# class Cat(Mammal):
#     pass
#
#
# dog1=Dog()
# dog1.walk()
# dog1.bark()
# cat1=Cat()
# cat1.walk()


##modules

# import converters
#
# print(converters.lbs_to_kg(2))
# print(converters.kg_to_lbs(2))

# from converters import kg_to_lbs
# print(kg_to_lbs(10))

# import utils
# numbers=[int(num) for num in input('Numbers: ').split()]   ##take a list as input
# print(utils.find_max(numbers))


##packages

# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce import shipping
# shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping
# calc_shipping()


##python library (random value)

# import random

# for i in range(4):
#     print(random.random())

# for i in range(4):
#     print(random.randint(10,100))

# members=['Panku','Voktho','Santona','Kamona','Rahul']
# leader=random.choice(members)
# print(leader)


##assignment(dice game)

# class Dice:
#     def roll(self):
#         import random
#         x = random.randint(1, 6)
#         y = random.randint(1, 6)
#         return x, y  # tuples
#
#
# dice1 = Dice()
# result = dice1.roll()
# print(result)

##Directories

# ( ##Absolute path......
        ##c:\Program Files\Microsoft

        ##Relative path
        ##like ecommerce )

# from pathlib import Path
# # path1=Path('ecommerce')
# # print(path1.exists())
# # path2=Path("emails")
# # #path2.mkdir() #make e new directory
# # path2.rmdir() #remove
#
# path3=Path() #no argument means current directory
# ##print(path3.glob('*.*')) ##search for files
#
# for file in path3.glob('*.xlxs'):  ## path3.glob('*.*) or ('*.py") or ('*.xls") etc.
#     print(file)

### Excel File

# filename = input("Filename: ")
# from automationExcel import process_workbook
#
# process_workbook(filename)
